import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

tab = pd.read_csv(r"D:\人工智能\analysis\列联表.csv", index_col=0, encoding="utf-8-sig")

fig, axes = plt.subplots(1, 2, figsize=(13, 5.4))

sns.heatmap(tab, annot=True, fmt="d", cmap="Blues", cbar=False,
            linewidths=.6, linecolor="white", ax=axes[0])
axes[0].set_title("父母职业类别列联表（人数）", fontsize=13)
axes[0].set_xlabel("母亲职业类别")
axes[0].set_ylabel("父亲职业类别")

pct = tab.div(tab.sum(axis=1), axis=0) * 100
sns.heatmap(pct, annot=True, fmt=".0f", cmap="Oranges", cbar=False,
            linewidths=.6, linecolor="white", ax=axes[1],
            vmin=0, vmax=100)
axes[1].set_title("按父亲职业分行看分布（行百分比 %）", fontsize=13)
axes[1].set_xlabel("母亲职业类别")
axes[1].set_ylabel("")

for ax in axes:
    ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig(r"D:\人工智能\analysis\父母职业关联_热力图.png", dpi=150, bbox_inches="tight")
print("已生成热力图")
