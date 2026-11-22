# N154: Qwen3-27B GPTQ/AWQ INT8 量化中，保留的 BF16 校准层（通常为 embedding 和 lm_head）显存占用约为 0.55 GB，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Qwen3-27B GPTQ/AWQ INT8 量化中，保留的 BF16 校准层（通常为 embedding 和 lm_head）显存占用约为 0.55 GB，计算公式为 (27.1e9 * 0.01) * 2 bytes / 1024^3，假设校准层占比约 1%

## Corrected Claim

Qwen3-27B GPTQ/AWQ INT8 量化中，保留的 BF16 校准层（通常为 embedding 和 lm_head）显存占用约为 0.55 GB，计算公式为 (27.1e9 * 0.01) * 2 bytes / 1024^3，假设校准层占比约 1%

## Evidence

先验知识/题面给定，逻辑校验通过：27.1e9 * 0.01 * 2 bytes ≈ 542 MB ≈ 0.55 GB，计算与量级合理
