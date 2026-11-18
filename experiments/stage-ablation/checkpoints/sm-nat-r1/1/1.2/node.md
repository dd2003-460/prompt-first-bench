# N6: LFU相对LRU增益上界估计方法：ΔH_max = H_LFU - H_LRU ≤ (1 - 1/β) * (1 - 1/α) * ρ_correction，其

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

LFU相对LRU增益上界估计方法：ΔH_max = H_LFU - H_LRU ≤ (1 - 1/β) * (1 - 1/α) * ρ_correction，其中ρ_correction为负相关修正因子，需通过联合分布积分计算

## Corrected Claim

LFU相对LRU增益上界估计方法：ΔH_max = H_LFU - H_LRU ≤ (1 - 1/β) * (1 - 1/α) * ρ_correction，其中ρ_correction为负相关修正因子，需通过联合分布积分计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU versus LRU hit ratio improvement upper bound Pareto workload
