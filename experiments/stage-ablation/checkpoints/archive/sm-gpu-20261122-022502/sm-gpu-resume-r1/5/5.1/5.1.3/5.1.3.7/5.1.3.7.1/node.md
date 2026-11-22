# N870: Qwen3-27B 在 BF16 精度下的完整权重显存占用为 54GB (27B * 2 bytes)，INT4 (W4A16) 量化后权重显存占用为 13.5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N272

## Claim

Qwen3-27B 在 BF16 精度下的完整权重显存占用为 54GB (27B * 2 bytes)，INT4 (W4A16) 量化后权重显存占用为 13.5GB (27B * 0.5 bytes) + 0.2GB (量化常数/Scale)，此处取 13.5GB 为理想下界，实际部署需预留 1-2% 开销，即 13.65-13.77GB。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的完整权重显存占用为 54GB (27B * 2 bytes)，INT4 (W4A16) 量化后权重显存占用为 13.5GB (27B * 0.5 bytes) + 0.2GB (量化常数/Scale)，此处取 13.5GB 为理想下界，实际部署需预留 1-2% 开销，即 13.65-13.77GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下为54GB，INT4量化后权重约为13.5GB，计算逻辑自洽且符合工程常识。
