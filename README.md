# 大数据与人工智能 · 学习仓库

> 作者：步文萱（GitHub: [Sissi547](https://github.com/Sissi547)）
> 本仓库是《大数据与人工智能》课程的个人学习仓库，收录 AI 通识课件、Python 四节基础课件、以及"语法到 AI 应用"的完整学习地图与八份概念学习资料。

## Python 学习路线（python-course/）

**总入口：[学习地图](python-course/学习地图.html)** —— 4 次课 × 90 分钟（每次课上下各 45 分钟：上半场补语法、下半场做 AI 应用）。

| 课次 | 上半场（45 min · 语法） | 下半场（45 min · AI 应用） |
|------|------------------------|---------------------------|
| 第 1 次 | 函数与模块 | AI 是什么：机器学习入门 |
| 第 2 次 | 正则表达式与 CSV | 文字变数字：词袋模型 |
| 第 3 次 | 类与对象 + 异常处理 | 情感分析实战 |
| 第 4 次 | 推导式、排序与计数 | 文本分类 + 结业项目 |

**概念学习资料目录：[学习资料/index.html](python-course/学习资料/index.html)**（含概念关联图）

| # | 概念 | 类型 | # | 概念 | 类型 |
|---|------|------|---|------|------|
| 01 | [函数与模块](python-course/学习资料/01-函数与模块.html) | 语法 | 05 | [类与对象 + 异常处理](python-course/学习资料/05-类与异常处理.html) | 语法 |
| 02 | [AI 是什么](python-course/学习资料/02-AI是什么.html) | AI | 06 | [情感分析](python-course/学习资料/06-情感分析.html) | AI |
| 03 | [正则表达式与 CSV](python-course/学习资料/03-正则表达式与CSV.html) | 语法 | 07 | [推导式、排序与计数](python-course/学习资料/07-语法收尾.html) | 语法 |
| 04 | [词袋模型](python-course/学习资料/04-词袋模型.html) | AI | 08 | [文本分类 + 结业](python-course/学习资料/08-文本分类.html) | AI |

**基础四课（Python 入门）**：[第 1 课 初识 Python](python-course/第1课-初识Python.html) · [第 2 课 数据类型与字符串](python-course/第2课-数据类型与字符串.html) · [第 3 课 列表判断与循环](python-course/第3课-列表判断与循环.html) · [第 4 课 综合实战](python-course/第4课-综合实战新闻热词统计器.html)

## AI 通识课件（learning-materials/）

| 课件 | 主题 | 内容 |
|------|------|------|
| [agent.html](learning-materials/agent.html) | Agent 智能体入门 | Agent 是什么、与聊天机器人/自动化的区别、工作循环、四大部分、使用时机（含 5 题测验） |
| [skill.html](learning-materials/skill.html) | Agent Skill 入门 | Skill 是什么、SKILL.md 写法、三层加载、四步动手做第一个技能（含 5 题测验） |
| [llm-context.html](learning-materials/llm-context.html) | 大模型上下文入门 | 上下文与上下文窗口、token、两个坑、三大应对策略、实用技巧（含 5 题测验） |
| [concept-relationship.html](learning-materials/concept-relationship.html) | 概念关系总结 | 大模型、Agent、上下文、Skill 四者的关系图解 |

> 课件为独立 HTML 文件，下载后双击即可在浏览器打开，方向键翻页，课后测验一次一道、逐题呈现。

## 个人技能（.workbuddy/skills/）

- [bu-wenxuan](.workbuddy/skills/bu-wenxuan/SKILL.md) —— 步文萱的个人介绍技能，遵循 Agent Skills 开放规范（agentskills.io）编写。

## 内容来源

课件内容依据以下权威资料整理：

- Anthropic 工程博客：《Building Effective Agents》《Effective Context Engineering for AI Agents》
- IBM：《What is a context window?》《AI Agents》
- Agent Skills 开放规范：agentskills.io
- Python 官方中文教程：docs.python.org/zh-cn/3/tutorial/
- scikit-learn 官方文档：scikit-learn.org（机器学习、文本特征提取、朴素贝叶斯）
- SnowNLP 开源项目：github.com/isnowfy/snownlp

## 仓库结构

```
本仓库/
├── .workbuddy/
│   └── skills/
│       └── bu-wenxuan/
│           └── SKILL.md
├── learning-materials/
│   ├── agent.html
│   ├── llm-context.html
│   ├── skill.html
│   └── concept-relationship.html
├── python-course/
│   ├── 学习地图.html
│   ├── 第1课-初识Python.html
│   ├── 第2课-数据类型与字符串.html
│   ├── 第3课-列表判断与循环.html
│   ├── 第4课-综合实战新闻热词统计器.html
│   └── 学习资料/
│       ├── index.html
│       └── 01-…08-….html（八份概念学习资料）
├── README.md
└── .gitignore
```
