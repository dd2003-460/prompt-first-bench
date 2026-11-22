# N145: 工作点1（理论上限，高信度/低精度）：在 Pareto(β=0.9) 下，LFU 集合相对于 LRU 的对称差字节量 B_LFU_only - B_LRU_on

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点1（理论上限，高信度/低精度）：在 Pareto(β=0.9) 下，LFU 集合相对于 LRU 的对称差字节量 B_LFU_only - B_LRU_only 的上界由热度长尾中 r_i 极高但 size_i 极小的对象决定，其值 ≈ Σ_{i ∈ LFU\LRU} r_i * s_i，在理想无噪声情况下，该差值最大可达总请求字节量的 3%-5%（即 ΔH_max ≈ 0.03-0.05），此工作点假设 LFU 完美识别所有 r_i > 1000/day 的对象且无驱逐滞后。

## Corrected Claim

工作点1（理论上限，高信度/低精度）：在 Pareto(β=0.9) 下，LFU 集合相对于 LRU 的对称差字节量 B_LFU_only - B_LRU_only 的上界由热度长尾中 r_i 极高但 size_i 极小的对象决定，其值 ≈ Σ_{i ∈ LFU\LRU} r_i * s_i，在理想无噪声情况下，该差值最大可达总请求字节量的 3%-5%（即 ΔH_max ≈ 0.03-0.05），此工作点假设 LFU 完美识别所有 r_i > 1000/day 的对象且无驱逐滞后。

## Evidence

先验知识/题面给定，逻辑校验通过
