# N250: 工作点3（ρ 极限敏感性）：分析 M_byte 对 σ_logR/σ_logS 的敏感性。若 σ_logR=2.0, σ_logS=0.5（更极端的负相关分布）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点3（ρ 极限敏感性）：分析 M_byte 对 σ_logR/σ_logS 的敏感性。若 σ_logR=2.0, σ_logS=0.5（更极端的负相关分布），M_byte = 1 + 0.3*(4)*0.5 = 1.6。此时 k_max 增加 60%，H_byte 提升显著。此点用于界定 ρ=-0.3 假设下，若分布更偏斜，LFU/LRU 增益的上界。

## Corrected Claim

工作点3（ρ 极限敏感性）：分析 M_byte 对 σ_logR/σ_logS 的敏感性。若 σ_logR=2.0, σ_logS=0.5（更极端的负相关分布），M_byte = 1 + 0.3*(4)*0.5 = 1.6。此时 k_max 增加 60%，H_byte 提升显著。此点用于界定 ρ=-0.3 假设下，若分布更偏斜，LFU/LRU 增益的上界。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 + 0.3*4*0.5 = 1.6 正确，且符合敏感性分析中参数变化对指标影响的定性描述逻辑。
