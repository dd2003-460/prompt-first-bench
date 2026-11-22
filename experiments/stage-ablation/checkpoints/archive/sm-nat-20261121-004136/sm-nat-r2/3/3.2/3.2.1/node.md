# N46: 交互项 interaction_term 的定义与计算：定义为 LFU 因热度-大小负相关（ρ=-0.3）导致的‘计数精度损失’比例。具体为：在 ρ=-0.3 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

交互项 interaction_term 的定义与计算：定义为 LFU 因热度-大小负相关（ρ=-0.3）导致的‘计数精度损失’比例。具体为：在 ρ=-0.3 下，前 K 个 LFU 保留对象中，因大小较大而被 LRU 驱逐但 LFU 保留的对象，其带来的额外命中字节增益相对于 ρ=0 时的衰减比例。量化形式：interaction_term = (Δ_H_ρ=0 - Δ_H_ρ=-0.3) / Δ_H_ρ=0。

## Corrected Claim

交互项 interaction_term 的定义与计算：定义为 LFU 因热度-大小负相关（ρ=-0.3）导致的‘计数精度损失’比例。具体为：在 ρ=-0.3 下，前 K 个 LFU 保留对象中，因大小较大而被 LRU 驱逐但 LFU 保留的对象，其带来的额外命中字节增益相对于 ρ=0 时的衰减比例。量化形式：interaction_term = (Δ_H_ρ=0 - Δ_H_ρ=-0.3) / Δ_H_ρ=0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU LRU difference size popularity correlation interaction term
