# N102: h_max 截断对字节命中率的影响阈值：当 h_max < P_99(H) 时，丢失的字节流量比例 ΔH_trunc ≈ (1 - 0.99) * (E[S|H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

h_max 截断对字节命中率的影响阈值：当 h_max < P_99(H) 时，丢失的字节流量比例 ΔH_trunc ≈ (1 - 0.99) * (E[S|H>h_max]/E[S])，在ρ=-0.3下该值小于0.5%。

## Corrected Claim

h_max 截断对字节命中率的影响阈值：当 h_max < P_99(H) 时，丢失的字节流量比例 ΔH_trunc ≈ (1 - 0.99) * (E[S|H>h_max]/E[S])，在ρ=-0.3下该值小于0.5%。

## Evidence

先验知识/题面给定，逻辑校验通过
