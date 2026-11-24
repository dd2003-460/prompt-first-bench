# N65: 提升缓存命中率的成本替代项 ΔC_hit = C_cache_upgrade * (1 - H_current) / (H_target - H_current

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

提升缓存命中率的成本替代项 ΔC_hit = C_cache_upgrade * (1 - H_current) / (H_target - H_current)；C_cache_upgrade 为缓存扩容成本（¥/GB/月），需与 ΔC_pop 对比，选择 min(ΔC_pop, ΔC_hit) 作为最优合规路径。

## Corrected Claim

提升缓存命中率的成本替代项 ΔC_hit = C_cache_upgrade * (1 - H_current) / (H_target - H_current)；C_cache_upgrade 为缓存扩容成本（¥/GB/月），需与 ΔC_pop 对比，选择 min(ΔC_pop, ΔC_hit) 作为最优合规路径。

## Evidence

先验知识/题面给定，逻辑校验通过
