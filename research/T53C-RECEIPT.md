# T53C 回执：DeepResearch 类 agent 的 SOTA 分数表

- **repo URL**：https://github.com/dd2003-460/prompt-first-bench
- **branch**：`arena/f65a5a27-prompt-first-bench`
- **base commit**：`ac1b481`（T53 dispatch card）
- **交付物**：`research/sm-bench-sota-table.json`（+ 可重跑生成器 `research/build-sm-bench-sota-table.py`、校验器 `loop-artifacts/stages/04/verify-t53c.py`）

## 验收对照

| 要求 | 结果 |
|---|---|
| ≥2 个系统的分数落盘 | ✅ **12 个系统行**（12 行全部有数值分数） |
| 每个分数有 source_url | ✅ 12/12 有 http URL，且每条附 `verbatim_excerpt` 逐字摘录供复核 |
| 逐题分数 | ⚠️ 全部 `null` + 写明原因（5 题是 pfb 自建题，公开数据不存在，任务书要求标 null 不编） |
| 推荐 1 个主 baseline + 理由 | ✅ Tongyi DeepResearch (30B-A3B)，864 字四条理由 + 2 个备选 |

## 主 baseline 与理由（摘要）

**Tongyi DeepResearch (30B-A3B)**：开源权重 + 官方复现脚本 + 多榜 SOTA（GAIA 70.9 / FRAMES 90.6 / WebWalkerQA 72.2 / xbench 75.0），30.5B 总参 3.3B 激活可单机跑，且其技术报告自带 OpenAI/Gemini/Kimi/GLM 对照表，pfb 分数可直接插表定位。

**副 baseline**：DeepResearcher (7B) —— 唯一公开 NQ/TQ/HotpotQA/2Wiki 四项 F1 的开源深研 agent，用于「同口径 EM/F1」比较。

**不选 OpenAI Deep Research 作主 baseline**：闭源、无逐题数据、无法复跑，只能当引用型天花板。

## 三个必须知道的坑

1. **短答案 F1 ≠ 深研报告分**：DeepResearcher HotpotQA F1 52.8，但 DeepResearch Bench RACE 只有 10.77。pfb 这 5 题是短答案型 → 按短答案榜选 baseline，别按 RACE 排名选。
2. **RACE 分数是相对比值**，换参考报告整表平移：官网页 v1（Gemini 48.88 / OpenAI 46.98）与 ICLR camera-ready（49.71 / 46.45）不同；第三方 aiwiki.ai 的 82.3/80.7 无法复算，已判为不可用来源。表内统一用 ICLR 版，漂移记在 `contradictions.X1`。
3. **GAIA 两口径**：pass@1 **67.36** vs cons@64 **72.57**，JSON 里分字段，引用时必须注明。

## 证据级别

- 一手全文（论文表格逐字摘录）：DeepResearcher、Tongyi、LangChain ODR、Gemini DR、OpenAI DR(DRB)、Perplexity DR、Kimi、DeepResearch Bench camera-ready 全表
- 一手官网：OpenAI deep research blog（GAIA/HLE）
- 二手转引（已在 notes 标注）：Search-R1、R1-Searcher（数字出自 DeepResearcher Table 1）
- 未采信：WebSailor-v2 74.1（仅聚合站）、aiwiki.ai RACE 数值

未改任何代码（本次只新增 research/ 与 loop-artifacts/ 文件）。
