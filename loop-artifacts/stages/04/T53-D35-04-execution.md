# T53-D35 阶段 04：执行与核验（含返工回环）

- 上游：02 调研台账 + 02.5 交叉核验
- 产出：`modules/F-theory/gradient-descent/litsurvey/2026-11-13-d35-realworld-vs-analytic-optimization-survey.md`（373 行）、`search-log-d35.json`、根索引 F 行更新、本文
- verifier：`loop-artifacts/stages/04/verify-d35.py`（21 项机检）
- 边界：本阶段才允许读/写 04 产物；02 未被回改（02 中不含 04 引用）

## 1. 执行步骤

1. 依 02 台账把 13 条 ① 来源与 13 条 ② 来源编进附录 A（每条标级 + read_level + 用途）。
2. 按 Q1 > Q2 > Q4 > Q3 顺序写 §2/§3/§4/§5；Q3 因无新实证只做口径加固并压 conf 到 0.66。
3. 把 02.5 的 C1–C5 五条对抗攻击落成 §8（4 条）并逐条写"对结论的影响"。
4. 写 §7「A vs B vs 结合」，把提案落到 `experiments/stage-ablation/s5_state_machine.py` 的**真实字段**上：
   - `S_alpha_corrected()` / `redundancy_score()` / `ObjectiveConfig.redundancy_penalty_beta=3.0` / `stop_std_max=0.06` / `classify_edge` 的 edge taxonomy / `NodeRecord.retrieval_sources`（D32）——均为本轮读源码确认，不是猜测。
5. 写 §11 勘误表（3 处 ID 错误 + 1 处补全）。
6. 跑 verifier，按 FAIL 回环修订（见 §3）。

## 2. 与 S5 现有设计的对齐结论（执行中发现，非文献结论）

- S5 **已有** 反塌缩机制：`S_α = Σ[n·ln kₙ + α·kₙ·ln n] − β·redundancy·n`，β=3.0（2026-11-11 标定，罚项≈structural 的 5%）。
- S5 **已有** 方差守卫：`stop_std_max=0.06`（P5 回标，1σ），但它的语义是"采样噪声大就别计数停止"，**不是**非平稳守卫。
- S5 **缺** 三项：① 探索项（只有反冗余，没有"往未访问子空间走"的正向激励）；② drift 监控（无 retention/重跑一致性检查）；③ 外部触发的重分解（现状靠人工改配置重跑）。
- 因此 D35 的增量是**加三项、不改既有项**，与"调研不改代码"约束一致（本任务只出方案，不动 `s5_state_machine.py`）。

## 3. verifier 返工回环记录（真实执行）

**第一次运行**：`fails=4 / 21`

| FAIL | 原因 | 处置 |
|---|---|---|
| AC7b（未找到 conf 全 ≤0.3） | 附录 C 里"drift 预算-理论化"一条写了 conf 0.55 | **回到上游修订 survey**：该行按"搜了没找到"纪律降为 0.30，并保留"需 Lead 二次交叉验证"的运行性含义；同步改 `search-log-d35.json` 的同一字段 |
| AC10（阶段工件缺 04/04.5） | 尚未写本文件与 04.5 | 本阶段补齐 |
| AC11b（索引 F 行未提 D35） | 索引未更新 | 只改第 15 行 |
| AC12（回执缺） | 未写 | 写 `research/T53-D35-RECEIPT.md` |

**处置原则**：AC7b 属"结论强度超证据"型错误 → **改结论不改判据**（conf 下调），不是把 verifier 放宽；AC10/AC11b/AC12 属"交付物未落地"型 → 补产物。

**第二次运行**：结果见 `loop-artifacts/stages/04/T53-D35-04-execution.log`（由 verifier 直接 tee，见回执 §4）。

## 4. 本轮未做的事（明确边界）

- 未改 `experiments/stage-ablation/s5_state_machine.py`（只提方案）。
- 未改 F-旧 survey 文件本体（保留历史工件），勘误写在本文 §11 + 索引"剩余内容"列。
- 未检索 adversarial MDP / endogenous dynamics 理论（附录 C 已登记为"未检索"，不是"未找到"）。
- 未重研 Goodhart 现象侧（引 T-PR-15，按其 ② 处理）。
