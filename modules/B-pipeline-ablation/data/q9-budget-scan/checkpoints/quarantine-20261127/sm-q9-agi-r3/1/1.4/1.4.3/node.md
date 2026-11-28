# N36: 在长序列 (>32k tokens) 推理中，Attention 计算的 FLOPs 随 seq_len^2 增长，而 TP 通信量随 seq_len 线性增长

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

在长序列 (>32k tokens) 推理中，Attention 计算的 FLOPs 随 seq_len^2 增长，而 TP 通信量随 seq_len 线性增长；因此随着序列长度增加，通信占比会从短序列时的 <5% 逐渐上升至长序列时的 15-25%。临界序列长度 L_crit 可由公式 L_crit = sqrt(Compute_FLOPs_per_token * Bandwidth / Communication_Factor) 估算，对于 V100 TP=4 27B 模型，该临界点通常在 16k-24k tokens 之间。

## Corrected Claim

在长序列 (>32k tokens) 推理中，Attention 计算的 FLOPs 随 seq_len^2 增长，而 TP 通信量随 seq_len 线性增长；因此随着序列长度增加，通信占比会从短序列时的 <5% 逐渐上升至长序列时的 15-25%。临界序列长度 L_crit 可由公式 L_crit = sqrt(Compute_FLOPs_per_token * Bandwidth / Communication_Factor) 估算，对于 V100 TP=4 27B 模型，该临界点通常在 16k-24k tokens 之间。

## Evidence

父节点级核验未通过：不完备（子节点之间存在明显的逻辑断层和覆盖缺失。父节点核心论述的是'随序列长度增加，通信占比上升'以及'临界序列长度 L_crit'的估算。然而，三个子节点全部聚焦于固定场景（seq_len=32k 或硬件常数），完全缺失了对'序列长度变化如何影响 FLOPs 与通信量比例'这一动态过程的分解，也未包含父节点中明确提到的 L_crit 计算公式及其推导逻辑。此外，子节点3中的具体数值（如8.6 TFLOPs）与父节点提到的通用公式缺乏直接映射，导致无法从子节点推导出父节点的结论。）

## Search Query

tensor parallelism communication compute ratio scaling with sequence length critical point
