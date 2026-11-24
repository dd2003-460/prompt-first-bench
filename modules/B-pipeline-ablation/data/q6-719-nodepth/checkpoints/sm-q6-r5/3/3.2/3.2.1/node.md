# N70: 出网流量 Traffic_out 的缓存修正：Traffic_out_effective = Total_Download_Traffic * (1 - H_e

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

出网流量 Traffic_out 的缓存修正：Traffic_out_effective = Total_Download_Traffic * (1 - H_effective)，其中 Total_Download_Traffic 为2TB/天，H_effective 为有效缓存命中率（引用 N12，公有云约90%，自建约80%）；因此公有云实际出网流量约 200GB/天，自建约 400GB/天；此修正至关重要，因为带宽成本仅针对实际传输流量，而非请求总量。

## Corrected Claim

出网流量 Traffic_out 的缓存修正：Traffic_out_effective = Total_Download_Traffic * (1 - H_effective)，其中 Total_Download_Traffic 为2TB/天，H_effective 为有效缓存命中率（引用 N12，公有云约90%，自建约80%）；因此公有云实际出网流量约 200GB/天，自建约 400GB/天；此修正至关重要，因为带宽成本仅针对实际传输流量，而非请求总量。

## Evidence

父节点级核验未通过：有冗余（子节点3和子节点4在结构上高度重复，均为公式代入计算过程，且仅因H值不同导致结果不同，属于同一逻辑分支下的参数化实例，可合并或简化。）
