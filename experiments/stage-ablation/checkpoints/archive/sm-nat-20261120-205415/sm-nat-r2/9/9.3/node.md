# N83: LFU增益上限的量化估算：假设K=128（基于C=128GB和平均大小1MB），F中对象平均大小为0.5MB（因高频对象倾向于较小，ρ=-0.3），L中对象平均

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LFU增益上限的量化估算：假设K=128（基于C=128GB和平均大小1MB），F中对象平均大小为0.5MB（因高频对象倾向于较小，ρ=-0.3），L中对象平均大小为1.5MB（因时间局部性可能包含较大对象），则H_LFU/H_LRU ≈ (0.5 * ∑h_F) / (1.5 * ∑h_L)，增益ΔH ≈ (H_LFU - H_LRU) * 100%，具体数值需通过联合分布建模计算。

## Corrected Claim

LFU增益上限的量化估算：假设K=128（基于C=128GB和平均大小1MB），F中对象平均大小为0.5MB（因高频对象倾向于较小，ρ=-0.3），L中对象平均大小为1.5MB（因时间局部性可能包含较大对象），则H_LFU/H_LRU ≈ (0.5 * ∑h_F) / (1.5 * ∑h_L)，增益ΔH ≈ (H_LFU - H_LRU) * 100%，具体数值需通过联合分布建模计算。

## Evidence

先验知识/题面给定，逻辑校验通过
