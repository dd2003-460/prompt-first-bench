# N55: 更新对象被命中的概率 P_hit_on_updated 的精确计算式：P_hit_on_updated = (1/N) * Σ_{i=1}^{N} (f_i /

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

更新对象被命中的概率 P_hit_on_updated 的精确计算式：P_hit_on_updated = (1/N) * Σ_{i=1}^{N} (f_i / F_total)，其中 f_i 为第 i 个对象的请求频率，F_total 为总请求频率，在均匀更新假设下等于平均请求频率占比，数值约为 1/100,000 * (1/100,000) * 50,000,000 = 0.005，即 0.5%。

## Corrected Claim

若 N=100,000 且假设均匀分布，P_hit_on_updated 应为 1/N = 0.001 (0.1%)；若按陈述中的乘法算式计算，结果应为 0.000005 (0.0005%)。原陈述数值 0.5% 无法由给定参数推导得出。

## Evidence

父节点级核验未通过：不完备（子节点仅修正了计算公式，未覆盖父节点中提到的具体数值估算（0.5%）及其推导过程，也未解释为何原公式在特定假设下不成立或新公式如何得出该数值，导致信息覆盖不全。）
