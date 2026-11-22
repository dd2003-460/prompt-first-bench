# N167: BF16 基线下 2x RTX 4090 的不可行性论证：总显存 48GB < 62GB 需求，即使启用 FP8 KV Cache (3GB)，总需求仍为 59

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

BF16 基线下 2x RTX 4090 的不可行性论证：总显存 48GB < 62GB 需求，即使启用 FP8 KV Cache (3GB)，总需求仍为 59GB > 48GB，因此必须采用权重量化 (如 INT8/FP8) 或 CPU Offload，这将导致 N49 描述的 'BF16 基线' 在 2x 4090 上物理不可行。

## Corrected Claim

BF16 基线下 2x RTX 4090 的不可行性论证：总显存 48GB < 62GB 需求，即使启用 FP8 KV Cache (3GB)，总需求仍为 59GB > 48GB，因此必须采用权重量化 (如 INT8/FP8) 或 CPU Offload，这将导致 N49 描述的 'BF16 基线' 在 2x 4090 上物理不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 显存为 48GB，小于 62GB 需求，且 59GB > 48GB，数学推导成立。
