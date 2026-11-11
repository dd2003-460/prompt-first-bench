# SM Bench SOTA 对标标准

> origin: ai (T53 AC4)
> 状态：v2（baseline = 本机模型 + 开源 deepresearch 框架，2026-11-11 成璐指令修订）

## 验收定义

**在 ≥5 道 deepresearch 类问题上，我们的管线（S5/T53）最终答案的 judge 分 ≥ 开源 deepresearch 框架（同一本机模型驱动）在同题上的分数。**

"打赢"不是节点数更少、不是更快——是**答案质量**（数字对不对、对比/单位对不对）。

## Baseline 定义（v2 · 2026-11-11 修订）

**核心原则**：同一模型（Qwen3-27B @8787），不同策略。主对比对象是"我们的管线（S5/T53）" vs "通用开源 deepresearch 框架"在同一模型上的表现差异。状态机（s5_state_machine.py）只是我们管线内部的候选臂之一，预期分数更低，不与 baseline 平级。

| 角色 | 内容 | 说明 |
|------|------|------|
| 实验组（主） | 我们的管线 S5/T53 | 目标函数驱动的 decomp+verify+rework+stop 流程 |
| 内部候选臂 | s5_state_machine.py | 管线内部实现之一，预期分数低于主臂，非独立主角 |
| 对照组 | 开源 deepresearch 框架 + Qwen3-27B | 当前活跃维护的 agent 框架 |

**开源 deepresearch 框架候选** [待核验：选哪个]：
- OpenHands (All-Hands-AI) — 2025-2026 活跃，支持本地 LLM via OpenAI-compatible API
- LangGraph + create_react_agent — 灵活，可配 search tool
- AutoGPT (agpt-co) — 老牌，但 2025 后活跃度下降
- CrewAI — 多 agent 协作，支持本地模型

**选择标准**：
1. 支持 OpenAI-compatible API（能指向 localhost:8787）
2. 有内置或易接的 web search 工具（我们的 bench 题需要搜索验证）
3. 2025-2026 仍活跃维护（GitHub 最近 3 个月有 commit）
4. 部署复杂度低（pip install + 配置文件即可跑）

**为什么不用公开分数表**：arena 调研确认（`research/sm-bench-sota-table.json`），我们的 5 题是自建 bench，不属于任何公开 test set，所有系统逐题分数均为 null。唯一可行的对比方式 = 本地复跑。

## Judge 口径

- **Judge**: B-face qwen2.5-7b (localhost:1234)，异族（生成端是 Qwen3.8-27B）
- **Rubric**: 每题满分 1.0 = 0.5（核心数字正确）+ 0.5（对比/单位/百分比正确）
- **聚合**: n=3 runs, median
- **tie-break**: 状态机 ≥ baseline 即算"打赢"（平局算赢）

## 题目选择（≥5 道）

当前候选（`tasks/T53C-bench-dispatch.md` 中已列）：
1. H200 TDP vs H100 SXM（GPU 硬件参数 + 百分比对比）
2. Transformer heads: 原始论文 vs GPT-3（论文事实 + 倍数计算）
3. HotpotQA 标注数 + compositional 比例（数据集元信息）
4. LLaMA 2 70B 参数量 + 训练 token 数（模型规格）
5. DeepSeek-V3 MoE 总参数/激活参数/ratio（架构参数）

## 执行流程

1. 选定开源 deepresearch 框架 → 配置指向 localhost:8787 → 跑 5 题 → 收集答案
2. 我们的管线（S5/T53）跑同样 5 题 → 收集最终答案 + 节点数 + 耗时；状态机作为内部候选臂一并跑，用于内部对照
3. B-face judge 对各组答案分别打分（n=3, median）
4. 判定：≥5/5 打赢 → AC4 PASS；否则记录哪些题输了 + 原因分析

## 文件索引

- 派发任务书: `tasks/T53C-bench-dispatch.md`
- 状态机代码: `experiments/stage-ablation/s5_state_machine.py`
- 防泄漏 SOP: `research/sm-leak-sop.md`
- SOTA 分数表（参考用，非主 baseline）: `research/sm-bench-sota-table.json`
- 本文件: `research/sm-bench-sota-criteria.md`