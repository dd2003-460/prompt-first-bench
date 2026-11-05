# 阶段 04：执行与结果核对 — RUBRIC-V3-FULL-AUDIT / G1

> goal: rubric-v3-audit-g1 · 2026-10-30 · owner: agent

## A1 · 机判脚本核验（r108 已入库，本轮重跑验证）✅

- 文件：`bench/rubric-v3/ablation/scripts/assert-g1-audit.py`（137 行）+ `scripts/g1-sample-cells.json`（75 cell 样本清单）——r108 随 G2 收口入库，本 goal 补齐 loop 工件。
- 重跑输出（逐字，exit 0）：
```
PASS A1 matrix-structure 8x31 h∈{0,1} evidence-policy
PASS A2 o3-recompute 24/24 exact match stats-recomputed.json
PASS A3 frozen-read-only hit-matrix/prior-estimates/judge-blindtest 未被本脚本写入
PASS A4 sample-deterministic seed=20261030 n=75 (h=1:35 h=0:40)
SIGNAL S1 evidence-verbatim sampled-h1-all-pass (35 cells checked)
SIGNAL S2 ptile-vs-hitrate spearman orig=0.456 new=0.6291; cross-judge rho=0.688
SIGNAL S2 LOW-CORR orig judge p̃ 与 8run 经验命中率相关弱 (ρ=0.456<0.5) → 系统性偏差信号
SIGNAL S3 binomial-flags n=3: N-1(zero-hit,p_orig=0.45,P_allmiss=0.0084); N-1.1(all-hit,p_orig=0.35,P_allhit=0.000225); N-5.3(all-hit,p_orig=0.05,P_allhit=0.000000)
SIGNAL S4 w2-cross-judge-gap top3: N-2.1(Δ4.91); N-1.3.1(Δ4.32); N-3.2.2(Δ3.74)
RESULT: all PASS, signals logged
```
- 确定性复核：连跑两次输出逐位一致（seed 20261030 固定抽样）。
- W3/W4 分数另对 stats-w3w4.json 独立复算：W3 × 8run + W4 × 8run 全部精确一致（容差 5e-5），补全 A2 的 24→40 个分数覆盖。

## A2 · 矛盾清单交付物落盘 ✅

- 文件：`bench/rubric-v3/ablation/G1-contradiction-audit.md`（新建，非冻结文件）
- 内容：C1-C4 四类矛盾（每条带 evidence 引用）+ 双 judge 31 节点全量对照表 + 四方案分数/top-5 表 + 口径声明（形式 vs 语义一致率分句）
- 关键数字（全部可复算，脚本 + 手工双重验证）：
  - 形式一致率（h=1 方向）：抽检 35/35 evidence 逐字命中 run 原文 = **100%**；h=0 方向未覆盖（S1 固有边界）；语义级独立重判 unverified（工具纪律禁 subagent，登记降级）
  - 抽检覆盖度：75 cell 落在 30/31 节点（仅 N-5.1 未抽中）
  - C1：ρ_orig=0.456（LOW-CORR，粗刻度限制已注明）；C2：N-1/N-1.1/N-5.3 三红旗
  - C3：零命中高 p̃ 清单（orig 口径 3 节点 / new 口径 6 节点）
  - C4：W3 global top-5 gold 计数 orig 3/5 → new 1/5 翻转，top-5 进出 3 席（观测层，根因移交 g2-rootcause.md）
- 新 judge 口径复算发现（供 G3 消费）：
  - W2-new 分数 {run1:0.3722, run2:0.3531, run3:0.3248, run4:0.2569, run5:0.2040, run6:0.3697, run7:0.3469, run8:0.3241} —— run1 反超 run6 成为第一（orig W2 下 run6 第一）
  - W3-new 分数 {run1:0.4107, run2:0.3549, run3:0.3268, run4:0.2505, run5:0.1923, run6:0.4127, run7:0.3691, run8:0.3432} —— run6 保持第一，但 run1/run6 差距从 0.0301 缩到 0.0020
  - per-run top-5 构念效度（strict gold 集 {N-2.1,N-3.2.2,N-2,N-4,N-1.3}）：**四个方案下没有任何一个 run 达到 ≥3 标记**（max=2，出现在 run1/run6/run7/run8 的部分方案）；run4/run5 在全部四方案下均为 0 标记——「per-run top-5 ≥3/5」口径比 blindtest 用的 global top-5 更不可能通过，这是判据设计的新证据点（移交 G3/G6）

## A3 · loop 工件 + current-goal 改写 ✅

- 六阶段工件：stages/01..04.5 前缀 RV3G1- 齐全（本文件为 04）
- tasks/current-goal.md 已改写为本 goal（五字段格式）

## A4 · commit + push（本步骤执行中）

## A5 · goal-queue + CONTINUE_MSG 更新（A4 后执行）

## 未完成项与诚实保留

- **语义级独立重判未执行**（任务书「随机 30% 节点独立重判报一致率」的完整口径）：ralph-loop-runner 工具纪律禁止开 subagent，本轮以 S1 evidence 逐字核验作为形式一致率交付，语义一致率标 unverified。建议后续用 arena 通道对 75 样本 cell（清单已落盘，可直接复用）做盲重判补数。
- web-llm 交叉询问三 provider 失效（回执 loop-artifacts/prompt-first/02-web-llm-cross-check.md）→ 按失败降级继续，外部文献线索标 unverified。
- C3 六节点的 rationale 细读未做（只列清单不定论）——属人工判断范畴，移交后续。
- 关键判读分支检查：A1 重跑零 FAIL → F1 数据自洽成立，无需回 02；C4 top-5 diff 与 judge-blindtest-r1.json 落盘值一致（无修正触发）。