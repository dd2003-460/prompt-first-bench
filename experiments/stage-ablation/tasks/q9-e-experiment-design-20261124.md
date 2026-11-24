# Q9 E 实验分析设计（2026-11-24 22:35 · Lead 方向判断）

> origin: ai · 触发：今晚 D3 同步时发现 judge_v1（加权求和，补偿性）与 gold v2 优化目标（lexicographic，gate 不可补偿）的语义错位。Q9 的 E 预算实验尚未跑，units 刚建好（gold-q9-units.json, 710e72de3）——现在定分析设计，防止实验测错东西。

## 核心张力
- gold v2 目标：先过硬门（capability N-1 / reliability N-3，11 个 gate 叶 J1-J5/J9-J14），门内再 min T/C。门不过 = 方案不可行，cost/time 再高也没用。
- judge_v1.judge_run：total = Σ 命中×档位×权重，跨 unit 补偿。低预算 run 可能在 cost/time 叶拿高分，掩盖 gate 叶失败，judge_total 曲线看起来"还行"。
- 若 E 实验因变量 = judge_total → 测的是"补偿性质量"，不是 D 要的"最快可靠路径"。

## 端点定义（E 跑完后按此分析，不跑前冻结）
1. **主端点 = gate-passing 阈值**：per-budget 的 gate 叶命中率（11 个 gate 叶，命中=embedding 匹配+档位达标），找"gate 命中率首次达 100% 的最小预算节点数"。这才是 lexicographic 下"可行解出现"的位置。
2. **次端点 = 门内质量**：gate 全过的 run 子集内，cost/time 叶（N-2/N-4）的 judge_total 随预算的变化。只有主端点过了才有意义。
3. **judge_total 全样本曲线**：保留但降级为参考（与 GPU/Q6/Q7 三域曲线可比，但标注"补偿性口径，非 lexicographic"）。

## 可证伪预测（E 跑完检验，错了改设计）
**P1（gate 早饱和）**：gate 叶多为单事实判据（J1 显存公式、J6 电费公式、J9-J11 定义类），模型一次 decompose 就能写出，不需要多节点。预测 gate 命中率在 ~100-150 节点就饱和（远低于 cov 轴的 ~300 拐点），即"可靠覆盖"比"质量覆盖"便宜得多。
- P1 成立 → D 的预算控制假说加强：预算买的主要是质量深度，不是可靠性；"最快可靠路径"的可靠性下限在低预算就已达成，预算优化空间在 T/C 轴。
- P1 不成立（gate 命中率随预算缓慢爬升）→ gate 叶的命中依赖树的展开广度（同一事实要从不同节点角度才能被 embedding 匹配到），可靠性是预算敏感变量，E 的主端点曲线有信息量。
- 判别数据：per-budget × per-gate-unit 命中率矩阵（11×5 档），不需要新实验，E 的 run json + gold-q9-units.json 直接算。

## 与 GPU/Q6/Q7 三域 E 的关系
三域 E 用的是补偿性 judge_total（gold 无 gate 结构）。Q9 是第一个 lexicographic 题。若 P1 成立且 gate 阈值显著低于 cov 拐点，则"预算→可靠覆盖"与"预算→质量覆盖"是两条不同曲线——这是三域数据里没有的新维度，workshop §4.3 可加一节（若 Q9 E 数据够）。

## 待办（不阻塞，E 跑完后做）
- [ ] E 跑完：per-gate-unit 命中率矩阵 + 主端点阈值 + 次端点曲线
- [ ] P1 判决（成立/不成立）→ 更新本文 + workshop §4.3
- [ ] τ_cap/τ_rel 若 D 给了数值：gate 叶的"命中"从 embedding 匹配升级为数值达标（S-a 叶可算）
