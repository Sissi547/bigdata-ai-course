import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

df = pd.read_csv(r"E:\类别变量练习数据.csv", encoding="gbk")
df.columns = ["father", "mother"]
df["father"] = df["father"].astype(str).str.replace("\n", "").str.strip()
df["mother"] = df["mother"].astype(str).str.replace("\n", "").str.strip().replace("nan", np.nan)

gov = ["局", "法院", "纪委", "市委", "镇", "管委会", "街道", "公安", "监狱", "团委", "执法", "审计", "统战", "编办", "社区"]
soe = ["中铁", "中海油", "兵器工业", "水利水电", "二十一冶", "农行", "给排水", "银光聚银"]
inst = ["大学", "中学", "学校", "医院", "学院", "保健站", "中心", "广播电视", "管理处"]
indiv = ["个体", "店", "馆", "菜市场", "烟酒", "浴", "农资", "食府", "书店", "大市场", "汽修"]


def classify(x):
    if pd.isna(x):
        return "缺失"
    s = str(x)
    if any(k in s for k in ["家庭主妇", "家庭父亲", "家庭父母"]) or s == "无":
        return "家庭主妇/无业"
    if s == "个体" or any(k in s for k in indiv):
        return "个体经营"
    if any(k in s for k in soe):
        return "国有企业"
    if any(k in s for k in inst):
        return "事业单位"
    if any(k in s for k in gov):
        return "党政机关"
    if any(k in s for k in ["有限公司", "有限责任公司", "公司", "旅行社", "养殖", "工贸"]):
        return "民营企业"
    return "其他/未识别"


df["父亲职业类别"] = df["father"].map(classify)
df["母亲职业类别"] = df["mother"].map(classify)

un = df[(df["父亲职业类别"] == "其他/未识别") | (df["母亲职业类别"] == "其他/未识别")]
print("未识别条数:", len(un))
if len(un):
    print(un.to_string())

m = {"党政机关": "体制内", "事业单位": "体制内", "国有企业": "体制内", "民营企业": "民营", "个体经营": "个体", "家庭主妇/无业": "无业"}
d = df[(df["父亲职业类别"] != "缺失") & (df["母亲职业类别"] != "缺失")].copy()
d["父亲合并"] = d["父亲职业类别"].map(m)
d["母亲合并"] = d["母亲职业类别"].map(m)

order = ["体制内", "民营", "个体", "无业"]
tab = pd.crosstab(d["父亲合并"], d["母亲合并"]).reindex(index=order, columns=order, fill_value=0)
print("\n=== 4x4 列联表 ===")
print(tab.to_string())

chi2, p, dof, exp = chi2_contingency(tab)
n = tab.values.sum()
v = np.sqrt(chi2 / (n * (min(tab.shape) - 1)))
print("\nN=%d  chi2=%.3f  p=%.4f  dof=%d" % (n, chi2, p, dof))
print("min_expected=%.2f  cells_lt5=%d/%d" % (exp.min(), (exp < 5).sum(), exp.size))
print("CramersV=%.3f" % v)

diag = sum(tab.iloc[i, i] for i in range(4))
print("same_category=%d/%d=%.1f%%  expected=%.1f%%" % (diag, n, diag / n * 100, sum(exp[i, i] for i in range(4)) / n * 100))

rng = np.random.default_rng(42)
cnt = 0
for _ in range(10000):
    perm = rng.permutation(d["母亲合并"].values)
    t = pd.crosstab(d["父亲合并"], perm).reindex(index=order, columns=order, fill_value=0)
    if chi2_contingency(t)[0] >= chi2:
        cnt += 1
print("perm_p=%.4f" % (cnt / 10000))

df.to_csv(r"E:\类别变量练习数据_清洗.csv", index=False, encoding="utf-8-sig")
print("\n已保存: E:\\类别变量练习数据_清洗.csv")
print("\n父亲类别分布:\n" + df["父亲职业类别"].value_counts().to_string())
print("\n母亲类别分布:\n" + df["母亲职业类别"].value_counts().to_string())

# 保存列联表
tab.to_csv(r"D:\人工智能\analysis\列联表.csv", encoding="utf-8-sig")
print("\n列联表已保存: analysis\\列联表.csv")
