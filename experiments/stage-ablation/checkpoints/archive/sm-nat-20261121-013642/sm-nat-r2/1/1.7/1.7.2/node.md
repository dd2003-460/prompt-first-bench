# N50: B_LFU_only 的上界由热度分布尾部决定：在 Pareto(β=0.9) 下，LFU 保留的“高频但非最近”对象集合大小约为总对象数的 5%-10%（基于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

B_LFU_only 的上界由热度分布尾部决定：在 Pareto(β=0.9) 下，LFU 保留的“高频但非最近”对象集合大小约为总对象数的 5%-10%（基于 β 的累积分布截断），其贡献字节量 B_LFU_only ≈ N_total * P(freq > f_threshold) * E[size | freq > f_threshold] * r_avg

## Corrected Claim

B_LFU_only 的上界由热度分布尾部决定：在 Pareto(β=0.9) 下，LFU 保留的“高频但非最近”对象集合大小约为总对象数的 5%-10%（基于 β 的累积分布截断），其贡献字节量 B_LFU_only ≈ N_total * P(freq > f_threshold) * E[size | freq > f_threshold] * r_avg

## Evidence

先验知识/题面给定，逻辑校验通过
