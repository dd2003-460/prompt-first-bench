# N33: β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0.9) 的 CDF，计算前 K 个对象（K 由 N21 得出）占据的总请求比例；该值直接决定 LFU 的理论命中率上限 H_LFU_max ≈ C_head * (1 - Size_Penalty)。

## Corrected Claim

β=0.9 时头部对象流量集中度 C_head：C_head = (Σ_{i=1}^{K} f_i) / (Σ_{all} f_i)；利用 Pareto(β=0.9) 的 CDF，计算前 K 个对象（K 由 N21 得出）占据的总请求比例；该值直接决定 LFU 的理论命中率上限 H_LFU_max ≈ C_head * (1 - Size_Penalty)。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点2和子节点3本质上是同一公式在不同K值下的具体数值实例，存在高度冗余，应合并或作为参数表处理；此外，父节点明确提到C_head决定LFU理论命中率上限H_LFU_max ≈ C_head * (1 - Size_Penalty)，但子节点完全未涉及Size_Penalty的定义、计算或H_LFU_max的最终推导，导致完备性缺失。）
