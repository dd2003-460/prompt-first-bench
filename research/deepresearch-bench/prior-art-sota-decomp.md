# prior-art-sota-systems — 分解树（decomp · 2026-11-12）

任务：调研 LLM deep-research SOTA 系统现状与公开成绩，落盘 `research/prior-art-sota-systems.md`。
已有资产（②类，本轮读过的）：`sm-bench-closed-sota-v3.md`、`drb-leaderboard-gpt55.csv`、`drb-leaderboard-legacy.csv`、`sm-bench-sota-table.json`（已核验带 URL）、`sm-bench-framework-selection.md`。

## 正交子项 × 缺口

| # | 子项 | 要什么 | 缺口 / 来源档 |
|---|------|--------|--------------|
| 1a | OpenAI Deep Research 架构 | 单 agent 循环 vs multi-agent；o3-based | 官方 blog 未明说架构 → 需查 [待核验] |
| 1b | Gemini Deep Research 架构 | 同上 | 官方 blog/文档 [待核验] |
| 1c | Perplexity Deep Research 架构 | 同上（Pro search 多步） | [待核验] |
| 1d | GPT-Researcher 架构 | 单 agent 检索-综合循环（开源，我们实测锚点 n=10/6 空壳） | ① 框架文档 + 我们的实测 |
| 1e | AutoGPT researcher 类 | 定位澄清（通用 agent 平台非深研专用） | ② framework-selection 已有 |
| 2a | DRB 构造方式 | 100 题 PhD 级、50中/50英、22 领域、专家 rubric | ② sm-bench-closed-sota-v3 已记；需核 arXiv 2506.11763 |
| 2b | DRB judge 协议 | RACE（target/reference 相对分）+ FACT（引用抽取核验） | ② sota-table 已记公式；需核原文 |
| 2c | DRB 已知争议 | 版本漂移（官网 v1 vs ICLR camera-ready vs aiwiki）、空壳答案问题 | ② sota-table contradictions.X1 已记；空壳是我们实测新发现 |
| 3 | 成本口径 | 每题 token 成本 / 时间 | **最大缺口**——公开数据极少 [待核验] |
| 4 | 对标意义 | 本地 27B + prompt 管线选谁做基线、比什么指标公平 | ② sota-table recommended_baseline=Tongyi；需结合空壳发现重判 |

## 留空约定
- 查不到的具体数字标 `[待核验]`，不从记忆填。
- 论文自报分数 vs 第三方复现分数分开列（DRB 官网 v1 / ICLR camera-ready / aiwiki 三源已见矛盾）。
- 空壳答案（n=10 有 6 题空壳）是我们的实测锚点，作为「judge 对空壳不敏感」的实证证据写入 §2。