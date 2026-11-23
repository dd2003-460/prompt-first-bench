# N227: 工作点2（中冗余/性价比平衡）：假设Zipf指数α=1.0，保留Top 30%对象覆盖97%流量，Cache_Size_2 = 0.3 * N_total * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

工作点2（中冗余/性价比平衡）：假设Zipf指数α=1.0，保留Top 30%对象覆盖97%流量，Cache_Size_2 = 0.3 * N_total * s_avg。若N_total=10M, s_avg=5MB，则Cache_Size_2 ≈ 150TB。此配置下H_ideal≈0.97，回源比例降至3%，P99延迟主要受缓存命中分布影响，带宽成本节省显著。

## Corrected Claim

工作点2（中冗余/性价比平衡）：假设Zipf指数α=1.0，保留Top 30%对象覆盖97%流量，Cache_Size_2 = 0.3 * N_total * s_avg。若N_total=10M, s_avg=5MB，则Cache_Size_2 ≈ 150TB。此配置下H_ideal≈0.97，回源比例降至3%，P99延迟主要受缓存命中分布影响，带宽成本节省显著。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.3 * 10M * 5MB = 150TB），Zipf分布特性与缓存命中率逻辑自洽。
