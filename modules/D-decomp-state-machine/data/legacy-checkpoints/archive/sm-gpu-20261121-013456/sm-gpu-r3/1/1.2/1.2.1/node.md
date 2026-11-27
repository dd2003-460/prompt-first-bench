# N50: Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用为 27 GB，但 FP8 量化需额外的 Scale 因子存储（通常为 FP32，每 128 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用为 27 GB，但 FP8 量化需额外的 Scale 因子存储（通常为 FP32，每 128 个元素共享一个 Scale），导致额外显存开销约为 27 GB * (4/128) ≈ 0.84 GB，总权重显存约为 27.84 GB。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的权重显存占用为 27 GB，但 FP8 量化需额外的 Scale 因子存储（通常为 FP32，每 128 个元素共享一个 Scale），导致额外显存开销约为 27 GB * (4/128) ≈ 0.84 GB，总权重显存约为 27.84 GB。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于Scale因子的存储机制与不同量化粒度下的开销计算，子节点2专注于总显存的精确汇总及对父节点错误估算的纠正。两者在逻辑上互补（机制 vs 结论/纠错），内容不重叠且无矛盾，共同完整覆盖了父节点中关于FP8显存占用的所有关键争议点。）
