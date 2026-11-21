# Design · research-agi-budget（02-design，2026-11-22）

> 原则：最小改动 + 可回滚。每个改动项 = 目标文件 + 改动描述 + 回滚 + 验证（前后对照）。
> 依赖：B/C/E 的 LLM 调用类改动等 matched 批（pid 87154）完成；A 是批后数据回收。

## 改动项表

| # | 改动项 | 目标文件 | 改动描述 | 回滚方式 | 验证方法（前后对照） |
|---|---|---|---|---|---|
| K1 | A2 恢复记账 | `recover_sm_matched.py`（已提交 49f7599db） | `--apply` 模式：archive synth json → runs_sm_matched/ + 补元数据 + judge 分拆 | 删除 runs_sm_matched/ 里 recovered=true 的文件（archive 原始数据不动） | dry-run 21/21 映射验证已通过（depth vs sm log 交叉核对）；apply 后 `ls runs_sm_matched/` = 30 文件 |
| K2 | A3 matched stats | `ablation_stats.py`（复用） | 跑 30 SM + 30 bare 同负载对比 | 无（只读数据出报告） | stats-sm-matched.md 生成，含 Welch/MWU/δ/CI |
| K3 | B1 P1H_INDEX 去 TCO 框架 | `prompts.py` line 306 | "即时 / 短期运营 / 长期持有" → "与该决策相关的时间跨度" | git revert 该 commit（prompts.py 单源，byte-level diff 落盘） | 改前基线 = matched 批数据（带污染）；改后 = 1 轮 smoke（gpu，10min）节点数/depth 对比，不崩 + 时间维度节点仍存在 |
| K4 | B2 领域例子抽象化 | `prompts.py` 4 处（P3_VERIFY:164 / P4_SYNTHESIZE:202 / EDGE_*:355,371 / contradiction_scan:457） | 硬件规格/按字节按请求/TCO/prefill-decode → 抽象占位符 | 同 K3（同 commit） | smoke 同 K3；byte-level diff 落盘 `notes/prompt-diff-<date>.md` |
| K5 | B3 AGI 题 prompt 组装 | `prompts.py` 新增 `P1_L1_AGI`（或 spec 层注入目标定义段） | 通用规则（K3/K4 后）+ Q9-agi §题面目标定义段；不含 gold 骨架 | git revert；P1_L1_AGI 是新增常量，删除即回滚 | 不泄露审计：grep gold/Q9.md 的节点 ID/公式在 prompt 中零命中；smoke 1 轮跑通 |
| K6 | C merge 消融 | `merge_ablation.py`（已提交 0784cded7） | Arm A concat vs Arm B 0.4261，单变量 merge on/off | 无（新脚本，不碰生产路径） | Δdepth 判定：>0.02=merge 是元凶 / <−0.02=merge 有用 / ≈0=非主瓶颈 |
| K7 | E3 预算扫描 | `budget_scan_batch.sh`（已提交 0784cded7） | max_nodes 5 档×3 reps=15 runs，串行 | 无（新脚本）；runs_budget_scan/ 可整目录删 | 15/15 记账 + Pareto 均值表生成；每档节点数 ≈ 预算值（±20%） |
| K8 | D3 rubric | `gold/Q9.md` 判定点节 | 12 叶子 → 12 判定点（S-a/S-b/S-c 档），arena 扩树后同步 | 文件覆盖（v0 是草稿） | 判定点数 = 叶子数；每点有判据+档位 |

## 正交性自检

- K1/K2（数据回收）vs K3-K5（prompt）：数据 vs 代码，不重叠 ✓
- K3（P1H_INDEX）vs K4（4 处例子）：不同常量不同行，同 commit 但改动点正交 ✓
- K5（新增常量）vs K3/K4（改现有常量）：新增 vs 修改，不重叠 ✓
- K6（synth 路径）vs K3-K5（decompose prompt）：不同阶段 ✓
- K7（decompose 预算）vs K6（synth merge）：不同变量 ✓
- K8（rubric）vs K7（实验）：K8 是 K7 第二轮（q9-agi 题）的输入，依赖非重叠 ✓

## 执行顺序（批完成后）

1. K1（apply 恢复，零 LLM，~2min）
2. K2（stats，零 LLM，~5min）
3. K3+K4+K5（prompt 修复+AGI 题组装，1 个 commit，smoke 1 轮 ~15min）
4. K6（merge 消融，1 个 LLM run ~15min）
5. K7（预算扫描，15 runs ~6-8h，可后台跑）
6. K8（rubric，纯文本，D 醒来后随 gold 扩树）

## 不可逆/对外项

无。全部改动在工作区内，git 可回滚。APPROVALS.md 无需新增。

## 批前阻塞状态（2026-11-22 03:30）

- K1-K7 全部代码就绪（已提交），等批完成（~08:00-09:00）
- K8 等 D 确认 Q9-agi 题面（3 个 [待核验]）
- arena 交叉检验（模板 §4）登录过期，降级本地 conf-0.2，登录恢复后补
