# N89: Total 字节吞吐量的负相关修正项：Total_corr = Total_independent * (1 + ρ * Cov(Size, Heat)/σ_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Total 字节吞吐量的负相关修正项：Total_corr = Total_independent * (1 + ρ * Cov(Size, Heat)/σ_size/σ_heat)，其中 Cov(Size, Heat) 需根据 α=1.1 和 β=0.9 的联合分布特性估算，ρ=-0.3 导致 Total 相比无相关假设降低约 5-8%。

## Corrected Claim

Total 字节吞吐量的负相关修正项：Total_corr = Total_independent * (1 + ρ * Cov(Size, Heat)/σ_size/σ_heat)，其中 Cov(Size, Heat) 需根据 α=1.1 和 β=0.9 的联合分布特性估算，ρ=-0.3 导致 Total 相比无相关假设降低约 5-8%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

joint distribution size popularity negative correlation correction factor throughput
