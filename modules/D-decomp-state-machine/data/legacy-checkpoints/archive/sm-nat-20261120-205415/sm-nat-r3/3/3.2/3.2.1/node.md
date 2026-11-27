# N50: LFU可缓存对象数 K_LFU 的计算：K_LFU = C / E[S | H ≥ H_threshold_f]，其中 H_threshold_f 为LFU保留

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

LFU可缓存对象数 K_LFU 的计算：K_LFU = C / E[S | H ≥ H_threshold_f]，其中 H_threshold_f 为LFU保留对象的最低频率阈值，需通过迭代求解使得 ∑_{i=1}^{K_LFU} s_i ≤ C

## Corrected Claim

LFU可缓存对象数 K_LFU 的计算：K_LFU = C / E[S | H ≥ H_threshold_f]，其中 H_threshold_f 为LFU保留对象的最低频率阈值，需通过迭代求解使得 ∑_{i=1}^{K_LFU} s_i ≤ C

## Evidence

父节点级核验未通过：有冗余（子节点1提供了阈值H的估算逻辑，子节点2、3、4则是基于不同平均大小假设下的K_LFU具体数值解。虽然2、3、4在逻辑上是同一公式在不同参数下的实例化（存在冗余），但它们共同覆盖了从最优到最坏的性能边界，且与子节点1（阈值推导）在功能上正交（一个是推导输入，一个是计算输出）。然而，将三个具体的数值工作点作为独立的子节点略显冗余，因为它们本质上是同一个计算步骤在不同假设下的结果，可以合并为一个“多场景K_LFU估算”节点。）
