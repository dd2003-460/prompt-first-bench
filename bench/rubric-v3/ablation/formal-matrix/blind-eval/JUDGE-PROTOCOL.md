# 盲评判分协议与口径登记（judge-1 / judge-2）

> 本文件记录 `judge-1-scores.json`、`judge-2-scores.json` 的判分口径、与上游文件的冲突裁决、以及一处已发现的盲评泄漏。
> 两份 JSON 的结构按 `TASK-blind-eval.md` §输出 schema（`judge_id` / `scores.{doc}.{items,o3_claims,total_score,max_score}`）。

## 1. 口径冲突与裁决

| 来源 | 说法 | 处置 |
|---|---|---|
| `TASK-blind-eval.md` §评分要求 3 | 「每个 rubric item … 逐项打 **0/1/2** 分」 | **采纳**（任务书优先级最高） |
| `judge-packet-template.json` → `instructions` | 「按 rubric 条目打**二值分（0/1）**」 | 不采纳，仅作为 0/1/2 的语义锚点（2=完整满足 / 1=部分满足 / 0=不满足） |
| `TASK-blind-eval.md` §输出 schema 示例 | `max_score: 20` | 视为格式示意。真实分母 = 非 NA 条目数 × 2 |

**NA 项（7 个，不计入分母）**：`O4-E5_correctness`、`P1-E1_dispatch`、`P1-E2_timing`、`P2-E1`、`P2-E2`、`P2-E3`、`P3-E3_provider_receipt`。
**非 NA 条目 19 个 → `max_score = 38`。**

## 2. 19 个计分条目

```
O1  E1_included / E2_evidence / E3_depth_eligible
O2  E1_L1 / E2_L2 / E3_L3 / E4_closure
O3  claim_coverage
O4  E1_parameterized / E2_numeric_interval / E3_flip_target / E4_structural
P1  E3_source_ratio / E4_domain_count
P3  E1_independent_sources / E2_contradiction_record
P4  E1_termination_note / E2_boundary_type / E3_actionable_path
```

## 3. O1 低先验集合的判定方法

按 `judge-packet-template.json` 的 O1 note（「judge 对照同批次各 run 的候选集交集判定」），对 21 份答卷的候选集做交集统计（21 份全文关键词比对）：

- **默认先验（出现 ≥14/21）**：RTX 3090(21)、A100-80GB(20)、RTX 5090(19)、M5 Ultra(19)、RTX 4090(18)、A6000(18)、DGX Spark(14)
- **中间档（8–11/21）**：A100-40GB(11)、M5 Max(10)、2×3090(9)、
- **低先验（≤7/21）**：L40S(8→中间档边界)、5060 Ti(7)、H100(5)、5080(5)、RTX 6000 Ada(4)、V100(4)、2×5090(4)、4×3090(3)、P40(3)、4060Ti(3)、T4(2)、P100(2)、A5000(2)、MI210(2)、8×3090(2)、2×Mac(1)

判定采用 **≤7/21** 为低先验（L40S 8/21 归中间档，不计入）。`O1-E3_depth_eligible` 计分：低先验候选数 1–3 → 2；4–6 → 1；0 或 >6 → 0。

## 4. O3 折算与观察

31 条原子 claim 逐条判 `covered` / `not_covered`，并折算成 `O3-claim_coverage` 的 0/1/2：Judge-1 阈值 ≥20→2、15–19→1、<15→0；Judge-2 同阈值（独立重算 claim 覆盖）。

**本批实测覆盖率 14–21/31（45%–68%）**，且不可覆盖项是结构性的：`N-3.1`、`N-3.1.1`、`N-3.1.2`、`N-3.1.3`（gold 用 FLOPs / 峰值算力 / MFU 建模 prefill）与 `N-2.2`（调度效率子因子）在 21 份答卷中 **0 命中**——所有 run 都用「实测 prefill tok/s」代替了「计算量 ÷ 折扣算力」。这不是判分严苛，是 gold 树与 run 产出在 prefill 建模路径上的系统性分歧，建议在 O3 归因时单列。

## 5. 已发现的盲评泄漏（登记）

`TASK-blind-eval.md` §匿名映射（仅 Lead 持有，裁判不可见）**就在任务书正文里**，直接给出 A=V0-baseline … G=V3-sham 的完整映射。任何读到该文件的人都已失去盲态。

**处置**：两个裁判在判分时**忽略该表**，只依据 `doc-*.md` 正文打分；全程未读 `blind-eval/anon-mapping.json`（`blind-eval/` 目录本身也未列在任何一判的输入里）。建议后续把映射表从任务书移到 `anon-mapping.json` 一处，并在任务书里删掉该节。

## 6. 两判的执行实况（如实记录）

两遍判分由**同一 agent** 于同一会话内先后完成：Judge-1 打完 21 份并落盘后才开始 Judge-2，中途未回看 Judge-1 分数；Judge-2 在开判前**预先声明**了更严的字面判据（见 `judge-2-scores.json` 的 `note`）。

因此：

- 两判的**分数差异**是有效的「判据严格度敏感性」证据；
- 两判的**一致率（399 项中 389 项完全一致，97.5%；差 ≤1 项 100%）不能当作独立评分者间信度**——它不是两个独立评分者产生的。若需要真实 IRR，应由第二个独立 agent/人重跑 Judge-2 的 21 份。

## 7. 排名观察（不作结论，仅供归因）

Judge-1 总分（满分 38）：B2 38 / B1 37 / B3 37 / D3 37 / F2 37 / C2 36 / D1 36 / D2 36 / F1 36 / C1 35 / C3 35 / G3 35 / E1 34 / E2 34 / E3 33 / G1 33 / G2 33 / F3 31 / A3 30 / A1 24 / A2 24。

Judge-2 总分：B2 38 / B1 37 / B3 37 / D3 37 / F2 37 / D2 36 / F1 36 / C1 35 / C2 35 / C3 35 / D1 35 / E2 34 / E1 33 / E3 33 / G3 33 / G1 32 / G2 32 / F3 31 / A3 30 / A1 23 / A2 23。

两判的相对序一致：**A 组（两判均垫底）< E/G < C/D/F < B 组**。差距主要来自 `O1`（低先验候选）、`O3`（gold 覆盖）、`P4`（边界类型与终止注记）三支，其余条目基本饱和。
