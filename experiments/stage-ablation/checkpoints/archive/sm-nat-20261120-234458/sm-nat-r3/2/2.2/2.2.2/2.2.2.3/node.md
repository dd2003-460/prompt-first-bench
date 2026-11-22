# N118: 负相关ρ=-0.3对LFU增益的修正项：由于热门对象较小，LFU保留的Top K对象总字节数占比低于其请求占比，导致H_LFU_bytes < H_LFU_re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

负相关ρ=-0.3对LFU增益的修正项：由于热门对象较小，LFU保留的Top K对象总字节数占比低于其请求占比，导致H_LFU_bytes < H_LFU_requests，修正因子 C_ρ = E[S|Q ∈ Top K] / μ_S，估计值 < 1，具体值需通过联合分布计算。

## Corrected Claim

负相关ρ=-0.3对LFU增益的修正项：由于热门对象较小，LFU保留的Top K对象总字节数占比低于其请求占比，导致H_LFU_bytes < H_LFU_requests，修正因子 C_ρ = E[S|Q ∈ Top K] / μ_S，估计值 < 1，具体值需通过联合分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关意味着高频对象倾向于小尺寸，导致LFU保留的Top K对象平均大小小于全局平均大小，因此修正因子C_ρ < 1，逻辑自洽。
