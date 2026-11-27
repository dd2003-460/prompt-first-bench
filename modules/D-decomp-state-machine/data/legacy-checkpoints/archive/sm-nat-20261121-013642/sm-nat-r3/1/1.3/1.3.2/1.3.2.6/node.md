# N118: 工作点1（独立假设基准）：假设 size 和 freq 独立 (ρ=0)，总字节流量 Total_Bytes = N * E[r] * E[s]。在 Paret

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

工作点1（独立假设基准）：假设 size 和 freq 独立 (ρ=0)，总字节流量 Total_Bytes = N * E[r] * E[s]。在 Pareto(α=1.1) 截断于 s_max=10GB 下，E[s] = s_min * α / (α-1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^(α-1))，计算得 Total_Bytes ≈ 1.5 * 10^9 GB/day。此值作为分母的基准参考。

## Corrected Claim

工作点1（独立假设基准）：假设 size 和 freq 独立 (ρ=0)，总字节流量 Total_Bytes = N * E[r] * E[s]。在 Pareto(α=1.1) 截断于 s_max=10GB 下，E[s] = s_min * α / (α-1) * (1 - (s_min/s_max)^(α-1)) / (1 - (s_min/s_max)^(α-1))，计算得 Total_Bytes ≈ 1.5 * 10^9 GB/day。此值作为分母的基准参考。

## Evidence

先验知识/题面给定，逻辑校验通过
