# N177: Qwen3-27B 在 BF16 精度下的纯权重显存占用精确值 W_bf16 = 27.3e9 * 2 bytes = 54.6 GB；若采用 FP8 精度，权

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

Qwen3-27B 在 BF16 精度下的纯权重显存占用精确值 W_bf16 = 27.3e9 * 2 bytes = 54.6 GB；若采用 FP8 精度，权重占用 W_fp8 = 27.3e9 * 1 byte = 27.3 GB。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的纯权重显存占用精确值 W_bf16 = 27.3e9 * 2 bytes = 54.6 GB；若采用 FP8 精度，权重占用 W_fp8 = 27.3e9 * 1 byte = 27.3 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.3e9参数 * 2字节(BF16) = 54.6GB，27.3e9参数 * 1字节(FP8) = 27.3GB，计算准确且符合显存占用基本公式。
