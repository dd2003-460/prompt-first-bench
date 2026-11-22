# N42: 缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于热门对象较小，∑_{i=1}^{k_max} S_i 可能小于 128GB，导致 P_pollution 接近 0；若 ∑_{i=1}^{k_max} S_i 接近 128GB，则 P_pollution ≈ 0.05-0.1。

## Corrected Claim

缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于热门对象较小，∑_{i=1}^{k_max} S_i 可能小于 128GB，导致 P_pollution 接近 0；若 ∑_{i=1}^{k_max} S_i 接近 128GB，则 P_pollution ≈ 0.05-0.1。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于P_pollution公式在特定参数下的失效与修正（判定为0），子节点2聚焦于基于该修正结果计算最终命中率H_LRU_eff。两者在逻辑上是推导关系（前因后果），内容不重叠且无矛盾，故正交性成立。但父节点的核心任务是“估算P_pollution”，子节点2虽然使用了P_pollution=0的结果，但其主体内容是关于命中率H_LRU_eff的计算，这超出了父节点“P_pollution数值估算”的范畴，属于后续步骤，导致对父节点主题的覆盖不完整（父节点应仅关注P_pollution的定性/定量结论，而非下游指标）。）
