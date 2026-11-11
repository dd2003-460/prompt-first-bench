# SM Bench SOTA 对标标准

> origin: ai (T53 AC4)
> 状态：v1（SOTA 清单待 arena 调研确认）

## 验收定义

**在 ≥5 道 deepresearch 类问题上，状态机最终答案的 judge 分 ≥ 最新开源 SOTA 在同题上的分数。**

"打赢"不是节点数更少、不是更快——是**答案质量**（数字对不对、对比/单位对不对）。

## SOTA 候选基线 [待核验]

| 系统 | 来源 | 公开结果位置 | 备注 |
|------|------|-------------|------|
| OpenAI Deep Research (o3-pro) | OpenAI 2025.02 | 官方博客 + HLE leaderboard | 非完全开源，但分数公开可对标 |
| GPT-4o + tool-use (多跳) | 各论文 baseline | HotpotQA / 2WikiMultihop leaderboard | 经典多跳 QA SOTA |
| AutoGPT / AgentGPT 类 | GitHub | 各自 repo benchmark 节 | 开源 agent 框架 |
| Perplexity Sonar Pro API | Perplexity | 无公开 per-question 分数 | 可能不可用 |
| Qwen3-232B (本地/云端) | 阿里云 | 各 bench 报告 | 同族模型，不算异族 |

**选择原则**：
- 优先选有**逐题分数**公开的（不是只有 aggregate）
- 至少包含 1 个 LLM-based agent（不是纯 IR pipeline）
- 如果找不到逐题分数 → 退化为 aggregate EM/F1 对标（HotpotQA dev set）

## Judge 口径

- **Judge**: B-face qwen2.5-7b (localhost:1234)，异族（生成端是 Qwen3.8-27B）
- **Rubric**: 每题满分 1.0 = 0.5（核心数字正确）+ 0.5（对比/单位/百分比正确）
- **聚合**: n=3 runs, median
- **tie-break**: 状态机 ≥ SOTA 即算"打赢"（平局算赢）

## 题目选择（≥5 道）

当前候选（`tasks/T53C-bench-dispatch.md` 中已列）：
1. H200 TDP vs H100 SXM（GPU 硬件参数 + 百分比对比）
2. Transformer heads: 原始论文 vs GPT-3（论文事实 + 倍数计算）
3. HotpotQA 标注数 + compositional 比例（数据集元信息）
4. LLaMA 2 70B 参数量 + 训练 token 数（模型规格）
5. DeepSeek-V3 MoE 总参数/激活参数/ratio（架构参数）

**替换规则**：如果某题 SOTA 没有公开分数，换一道有的。最终 bench 必须保证 ≥5 道可对标。

## 执行流程

1. 状态机跑 5 题 → 收集最终答案 + 节点数 + 耗时
2. SOTA 分数从公开来源获取（arena 调研）→ 填入 `runs/sm-bench-sota-table.json`
3. Judge 打分 → 填表
4. 判定：≥5/5 打赢 → AC4 PASS；否则记录哪些题输了 + 原因分析

## 文件索引

- 派发任务书: `tasks/T53C-bench-dispatch.md`
- 状态机代码: `experiments/stage-ablation/s5_state_machine.py`
- 防泄漏 SOP: `research/sm-leak-sop.md`
- 本文件: `research/sm-bench-sota-criteria.md`