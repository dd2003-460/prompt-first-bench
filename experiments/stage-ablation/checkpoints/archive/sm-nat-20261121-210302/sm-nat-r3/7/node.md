# N21: LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 L

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Corrected Claim

LFU 相比 LRU 的提升上限受限于‘频率-大小’错配：当 β=0.9 且 ρ=-0.3 时，LFU 保留的热点对象平均大小 S_LFU_hot 显著小于 LRU 驱逐的平均大小 S_LRU_evict，提升百分点 Δ% ≈ (S_LRU_evict - S_LFU_hot)/S_LRU_evict * MissRate_LRU。

## Evidence

父节点级核验未通过：不完备（子节点在定义上正交，分别定义了 LFU 热点大小、LRU 驱逐大小和最终提升公式。但存在严重的不完备性：父节点中明确提到的核心概念‘频率-大小’错配（即相关性 ρ=-0.3）在子节点中完全缺失。子节点仅提供了基于热度分位数的边际期望计算（E[S|P]），忽略了频率与大小之间的负相关关系，导致无法解释为何 LFU 保留的 S 会显著小于 LRU 驱逐的 S（若仅看边际分布，两者可能接近），未能体现父节点强调的‘错配’机制。）
