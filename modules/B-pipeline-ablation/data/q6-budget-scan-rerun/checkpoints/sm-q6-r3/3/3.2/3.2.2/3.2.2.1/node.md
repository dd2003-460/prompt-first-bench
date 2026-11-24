# N214: 自建节点总峰值带宽 B_peak_total 的精确计算公式：若各POP点流量完全独立同分布，B_peak_total = B_avg_total × R_pg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

自建节点总峰值带宽 B_peak_total 的精确计算公式：若各POP点流量完全独立同分布，B_peak_total = B_avg_total × R_pg × sqrt(N_pops) / N_pops × N_pops = B_avg_total × R_pg × sqrt(N_pops)，其中 N_pops = 10，sqrt(10) ≈ 3.16，因此 B_peak_total ≈ 23.15 Mbps × 3.0 × 3.16 ≈ 219.4 Mbps；若流量部分相关（相关系数 ρ = 0.5），则 B_peak_total ≈ B_avg_total × R_pg × (1 + (N_pops - 1) × ρ)^0.5 ≈ 23.15 × 3.0 × (1 + 9 × 0.5)^0.5 ≈ 23.15 × 3.0 × 2.37 ≈ 164.7 Mbps

## Corrected Claim

自建节点总峰值带宽 B_peak_total 的精确计算公式：若各POP点流量完全独立同分布，B_peak_total = B_avg_total × R_pg × sqrt(N_pops) / N_pops × N_pops = B_avg_total × R_pg × sqrt(N_pops)，其中 N_pops = 10，sqrt(10) ≈ 3.16，因此 B_peak_total ≈ 23.15 Mbps × 3.0 × 3.16 ≈ 219.4 Mbps；若流量部分相关（相关系数 ρ = 0.5），则 B_peak_total ≈ B_avg_total × R_pg × (1 + (N_pops - 1) × ρ)^0.5 ≈ 23.15 × 3.0 × (1 + 9 × 0.5)^0.5 ≈ 23.15 × 3.0 × 2.37 ≈ 164.7 Mbps

## Evidence

先验知识/题面给定，逻辑校验通过：独立同分布下峰值带宽与平均带宽之比（峰值因子）随节点数增加呈 sqrt(N) 增长符合统计学原理（中心极限定理/方差叠加），数值计算 23.15 * 3.0 * 3.16 ≈ 219.4 正确；部分相关情形下使用 (1 + (N-1)ρ)^0.5 作为等效峰值因子也是处理相关随机变量峰值的常用工程近似，数值计算 23.15 * 3.0 * 2.37 ≈ 164.7 正确。
