# N283: H100 SXM5 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

H100 SXM5 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B (假设 n_layers=48, n_heads=32, head_dim=128, BF16)，KV_Cache ≈ 2 * 48 * 32 * 128 * 32768 * 2 bytes ≈ 25.8 GB，导致可用权重显存从 80GB 降至 ~54GB，需验证是否溢出或需分页。

## Corrected Claim

H100 SXM5 在 32K 上下文下的 KV Cache 显存占用计算：KV_Cache_Size = 2 * n_layers * n_heads * head_dim * seq_len * dtype_size。对于 Qwen3-27B (假设 n_layers=48, n_heads=32, head_dim=128, BF16)，KV_Cache ≈ 2 * 48 * 32 * 128 * 32768 * 2 bytes ≈ 25.8 GB，导致可用权重显存从 80GB 降至 ~54GB，需验证是否溢出或需分页。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2 * layers * heads * head_dim * seq_len * dtype_size），数值计算准确（2*48*32*128*32768*2 ≈ 25.77GB），显存占用推导符合H100 SXM5 80GB总显存减去KV Cache后的剩余可用权重显存逻辑。
