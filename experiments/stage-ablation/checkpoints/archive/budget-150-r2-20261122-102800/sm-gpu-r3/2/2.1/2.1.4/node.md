# N78: NVFP4/W4 量化对 Embedding 层的影响：Embedding 层通常不进行 4-bit 量化，保持 BF16，因此 4-bit 方案的权重显存 =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVFP4/W4 量化对 Embedding 层的影响：Embedding 层通常不进行 4-bit 量化，保持 BF16，因此 4-bit 方案的权重显存 = 1.36 GB (Embedding BF16) + 26.5B * 0.5 bytes (Rest INT4) ≈ 14.61 GB (略高于 N13 的 13.5 GB 估算)。

## Corrected Claim

NVFP4/W4 量化对 Embedding 层的影响：Embedding 层通常不进行 4-bit 量化，保持 BF16，因此 4-bit 方案的权重显存 = 1.36 GB (Embedding BF16) + 26.5B * 0.5 bytes (Rest INT4) ≈ 14.61 GB (略高于 N13 的 13.5 GB 估算)。

## Evidence

先验知识/题面给定，逻辑校验通过：Embedding层通常保持高精度（BF16）以避免语义损失，其余层量化为INT4（0.5 bytes/weight），计算逻辑自洽且数值量级合理。
