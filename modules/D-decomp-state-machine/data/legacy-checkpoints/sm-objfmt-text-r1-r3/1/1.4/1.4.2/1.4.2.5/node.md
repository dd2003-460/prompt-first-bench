# N115: FP8/INT8 精度下 KV Cache 显存占用：若 KV Cache 保持 BF16 (常见于 FlashAttention-2 默认配置)，则仍为 8.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N35

## Claim

FP8/INT8 精度下 KV Cache 显存占用：若 KV Cache 保持 BF16 (常见于 FlashAttention-2 默认配置)，则仍为 8.59 GB；若 KV Cache 也量化为 FP8/INT8 (需特定后端支持如 vLLM-FP8-KV)，则降至 4.29 GB。N35 直接复用 BF16 的 8.59 GB 假设 KV 未量化，此为保守估计。

## Corrected Claim

FP8/INT8 精度下 KV Cache 显存占用：若 KV Cache 保持 BF16 (常见于 FlashAttention-2 默认配置)，则仍为 8.59 GB；若 KV Cache 也量化为 FP8/INT8 (需特定后端支持如 vLLM-FP8-KV)，则降至 4.29 GB。N35 直接复用 BF16 的 8.59 GB 假设 KV 未量化，此为保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16 (16-bit) 到 FP8/INT8 (8-bit) 的量化理论上使显存占用减半，8.59 GB / 2 ≈ 4.295 GB，与陈述中的 4.29 GB 数值吻合，符合基本算术与工程常识。

## Search Query

vLLM FP8 KV cache quantization support
