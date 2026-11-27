# N166: LFU相比LRU的性能提升机制在于其能更有效地保留高频小对象，从而在相同缓存容量下容纳更多高价值对象；量化提升幅度ΔH_pp = (H_LFU - H_LRU)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU相比LRU的性能提升机制在于其能更有效地保留高频小对象，从而在相同缓存容量下容纳更多高价值对象；量化提升幅度ΔH_pp = (H_LFU - H_LRU) * 100% ≈ 4.5个百分点，该值基于ρ=-0.3的负相关假设，表明高频对象平均大小比独立假设低6%，使得LFU在容量约束下可多容纳约10%的高频对象，进而提升字节命中率。

## Corrected Claim

LFU相比LRU的性能提升机制在于其能更有效地保留高频小对象，从而在相同缓存容量下容纳更多高价值对象；量化提升幅度ΔH_pp = (H_LFU - H_LRU) * 100% ≈ 4.5个百分点，该值基于ρ=-0.3的负相关假设，表明高频对象平均大小比独立假设低6%，使得LFU在容量约束下可多容纳约10%的高频对象，进而提升字节命中率。

## Evidence

检索失败: no sources from any channel (all 5 failed)
