# N158: KV Cache 单 token 显存占用计算：对于 Qwen3-27B (假设 L=64, H_kv=8, D=128, BF16)，单个 token 的 K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

KV Cache 单 token 显存占用计算：对于 Qwen3-27B (假设 L=64, H_kv=8, D=128, BF16)，单个 token 的 KV Cache 大小为 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes ≈ 0.25 MB。32K tokens 的总占用为 0.25 MB * 32768 = 8192 MB = 8 GB。这与 N39 声称的 40.96 GB 存在巨大差异，表明 N39 的计算公式或参数有误（可能误将 Head Dim 当作 Total Dim 或层数重复计算）。正确值应为 8 GB (BF16) 或 4 GB (FP8/INT8 KV)。

## Corrected Claim

KV Cache 单 token 显存占用计算：对于 Qwen3-27B (假设 L=64, H_kv=8, D=128, BF16)，单个 token 的 KV Cache 大小为 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes ≈ 0.25 MB。32K tokens 的总占用为 0.25 MB * 32768 = 8192 MB = 8 GB。这与 N39 声称的 40.96 GB 存在巨大差异，表明 N39 的计算公式或参数有误（可能误将 Head Dim 当作 Total Dim 或层数重复计算）。正确值应为 8 GB (BF16) 或 4 GB (FP8/INT8 KV)。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存计算公式为 2 * L * H_kv * D * Bytes，代入参数 2*64*8*128*2 = 262,144 bytes (0.25 MB)，32K tokens 总占用 0.25 * 32768 = 8192 MB = 8 GB，计算无误。

## Search Query

Qwen3-27B KV cache size calculation 32k context
