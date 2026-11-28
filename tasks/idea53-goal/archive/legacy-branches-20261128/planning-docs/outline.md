# #53 短文大纲（成立分支 · T6）

> goal: idea53-cross-gradient · 2026-11-24 · 生死线已判成立（idea53-theory-flip.md）
> venue 双轨：NeurIPS'27 E&D（P 0.30）+ ICML'27 workshop（P 0.55）· arXiv 必挂
> 预注册：GOAL.md §0.5 @ eb1b0598c（17:39）早于数据 @ 718394ece（18:06）

## 1. Claim（一句话）
在非线性瓶颈判定（f(微架构因子)→瓶颈类型，因子交互）下，**深层微架构判断节点对瓶颈判断的增量贡献 = 它修正表面（浅层枚举）判断的量**，该量可闭式计算、随 rate-ratio 结构增大，且负对照（rate 全相等）归零——证明贡献来自微架构信息而非浅层转发。

## 2. 为什么是这个量（motivation，审稿第一问）
1. 非线性：瓶颈判定是组合函数（精度算力比 × workload 构成 × 标量占比 × 带宽）。实证 T5000：FP16 占 workload 30% 但交互后占 78% 时间 → 占比小≠贡献小。
2. 所以用信息论量非占比/ablation：线性归因系统性低估交互项。
3. 所以用树：可展开 + 支持正交完备性核对 + 逐层条件化=增量信息。
4. 深层节点信息增益 = 深层判断对表面判断的修正量（方向修正 + 粒度细化）。

## 3. 方法（surface-vs-deep，全闭式，无实验无 LLM）
- 浅层枚举 = 表面判断：假设 rate 全相等 → 时间∝workload → 瓶颈=主导 workload 类。
- 深层微架构判断 = 真实 rate ratio → t_i=f_i/rate_i → 瓶颈=argmax t_i。
- 深层信息增益 = flip rate（瓶颈类型翻转率）+ time shift（时间占比修正量）。
- 数据：4 硬件 spec（5090/T5000/4090/A100）+ workload 先验 Dirichlet(1,1,1,1)，N=40000 采样。
- 待补（T8）：flip/shift → 严格互信息 H(surface)−H(surface|deep)。

## 4. 结果
- 浅层枚举 43-56% workload 判错瓶颈类型（每硬件 flip rate 0.43-0.56）。
- 深层修正量 time shift 0.17-0.23（随 rate-ratio 结构）。
- 负对照 flat（rate 全=1）：flip=0, shift=0.0000（恰好归零）。
- D 三例全复现：T5000 50/50→80%、70/30→63%、5090 标量40%+issue砍半→慢40%。

## 5. 对照臂（防御）
- ① flat 占位硬件（rate 全等）→ 修正=0：解转发平凡性（深层信息非浅层转发）。
- ② 参数-深度重排：增益跟参数走（非 depth 标签）：解同义反复（判据去深度化）。
- ③ 层内类型对照：判断型 vs 枚举型节点贡献比较：解 type×depth 混淆。

## 6. 防御段（必含）
- **HARKing 声明**：判据+公式预注册 commit eb1b0598c（17:39）早于数据产出 718394ece（18:06），git log 可查。
- **转发平凡性回应**：flat 对照归零证明深层信息纯来自 rate-ratio。
- **同义反复回应**：参数-深度重排臂证明增益跟参数走，非 depth 定义驱动。

## 7. Limitation
- flip/shift 是可解释得分非严格 MI（T8 补 H(surface)−H(surface|deep)）。
- 4090/A100 无原生 FP4，fp4 rate 用 0.5×fp16 推 [待核验]。
- workload 先验 Dirichlet(1,1,1,1) 未建模真实 LLM 推理偏置。
- 单调性：修正量与 rate-ratio 结构相关，非仅极端度（A100>5090 打破严格单调）。

## 8. 结构（4-6 页 E&D / 5 页 workshop）
① claim ② motivation（非线性→MI→树→修正量）③ 方法（surface-vs-deep+闭式）④ 结果（flip/shift+flat 对照+三例复现）⑤ 对照臂×3 ⑥ 防御段 ⑦ limitation。
