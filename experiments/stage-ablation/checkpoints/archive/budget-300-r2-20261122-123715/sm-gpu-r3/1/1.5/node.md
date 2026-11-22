# N9: KV Cache 显存占用公式 = 2 × num_layers × hidden_size × seq_len × dtype_size / 1024^2 G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

KV Cache 显存占用公式 = 2 × num_layers × hidden_size × seq_len × dtype_size / 1024^2 GB；对于 Qwen3-27B (72 layers, 4096 hidden size)，在 32K 序列长度下，BF16 精度 KV Cache 需 ~36GB，FP8/INT8 需 ~18GB，W4 需 ~9GB。

## Corrected Claim

KV Cache 显存占用公式 = 2 × num_layers × hidden_size × seq_len × dtype_size / 1024^2 GB；对于 Qwen3-27B (72 layers, 4096 hidden size)，在 32K 序列长度下，BF16 精度 KV Cache 需 ~36GB，FP8/INT8 需 ~18GB，W4 需 ~9GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（2×72×4096×32768×2/1024^3 ≈ 36GB），数值量级合理。
