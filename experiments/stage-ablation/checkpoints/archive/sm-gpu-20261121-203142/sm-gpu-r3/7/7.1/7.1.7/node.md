# N335: RTX 4090 运行 Qwen3-27B W4A8 (4-bit 权重, 8-bit 激活) 时的显存占用细化：权重 6.75GB + KV Cache (B

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107, N108, N109

## Claim

RTX 4090 运行 Qwen3-27B W4A8 (4-bit 权重, 8-bit 激活) 时的显存占用细化：权重 6.75GB + KV Cache (BF16, 4GB) + 激活值 (BF16, 2GB) = 12.75GB；剩余显存 11.25GB 可用于扩展 Batch Size 或上下文，支持 B_max ≈ 5 (基于 4GB KV/req) 或 L_max ≈ 180K (基于 Batch=1)

## Corrected Claim

RTX 4090 运行 Qwen3-27B W4A8 (4-bit 权重, 8-bit 激活) 时的显存占用细化：权重 6.75GB + KV Cache (BF16, 4GB) + 激活值 (BF16, 2GB) = 12.75GB；剩余显存 11.25GB 可用于扩展 Batch Size 或上下文，支持 B_max ≈ 5 (基于 4GB KV/req) 或 L_max ≈ 180K (基于 Batch=1)
