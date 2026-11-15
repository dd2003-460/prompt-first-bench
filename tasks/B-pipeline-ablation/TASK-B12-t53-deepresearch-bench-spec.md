# T53 补充任务书：deepresearch 泛化 bench（≥5 题打赢 SOTA）

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

> origin: ai · 2026-11-15 · Lead 验收 T53-D35 后发出
> 上游：T53-D35 文献调研（14/14 AC 过，verifier fails=0）
> 本任务书是 t53-decomp-sm goal 的**核心验收标准**落地——T53-D35 只完成了调研子项，bench 跑分还没做。

## 目标

在 ≥5 道 deepresearch 类问题上，S5 状态机最终答案质量（judge 分）≥ 当前最新开源 SOTA 基准在同等题目上的分数。

## 验收标准（量化）

1. **题目数**：≥5 道 deepresearch 类问题（多跳推理 + 事实检索混合）
   - 已有 2 道（gpu 推理题 + drb 保险公司题），需新增 ≥3 道
   - 选题来源：现有 bench 题库 / deepresearch 公开 benchmark（如 GAIA、HotpotQA、BrowseComp）
2. **SOTA 对标**：每道题有 ≥1 个开源 SOTA 基线的公开分数
   - 候选：GPT-4o-based DeepResearch、OpenAI o3-pro、开源 agent（如 AutoGPT、MetaGPT）
   - 口径：异族 judge (B-face 7b) 打分 0-1，数字正确 0.5 + 对比/单位正确 0.5，n=3 median
   - SOTA 分数来源：论文/官方报告/公开 leaderboard，标注来源 + 日期
3. **judge 口径**：与 T53-D35 一致（异族 judge，n=3 median）
4. **产出**：
   - `experiments/stage-ablation/s5-sm-bench-report.md` 更新：≥5 题 × SOTA 对标表
   - 每题的 run 数据落盘 `experiments/stage-ablation/runs-s5-sm-<topic>.json`
   - SOTA 对标清单落盘 `modules/E-sota-benchmark/research/sm-bench-sota-criteria.md`（目前缺失）

## 约束

- **防泄漏**：状态机所有 prompt / 日志 / 中间产物不得包含题目原文（A6 约束）
- **不重复**：已有 2 道题的 run 数据直接复用，不重跑
- **SOTA 分数查不到就标 [待核验]**，不编

## 降级

arena 不可用 → 本地跑（conf-0.2），只降通道不降流程。

## 回执（必须）

完成后回执 JSON 必须含 `repo`（remote URL）+ `branch` + `commit_sha`（你 push 到的分支的 sha）。Lead 落盘前用 `git ls-remote` 核对 sha 存在——回执没指纹 = 未验证，不通过门禁。
