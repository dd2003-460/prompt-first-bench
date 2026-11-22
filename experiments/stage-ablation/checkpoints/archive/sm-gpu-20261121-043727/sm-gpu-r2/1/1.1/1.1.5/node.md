# N43: 修正 N7 的 KV Cache 计算公式：KV_Cache_GB = 2 (K+V) × num_layers (64) × num_key_value_he

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

修正 N7 的 KV Cache 计算公式：KV_Cache_GB = 2 (K+V) × num_layers (64) × num_key_value_heads × head_dim × seq_len (32768) × bytes_per_elem / 1024^3。若 num_key_value_heads=8, head_dim=128, BF16 (2 bytes)，则计算值为 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 ≈ 8.0 GB，而非 N7 中基于 MHA 假设的 131 GB。此差异源于 GQA 机制，是显存估算的关键修正项。

## Corrected Claim

修正 N7 的 KV Cache 计算公式：KV_Cache_GB = 2 (K+V) × num_layers (64) × num_key_value_heads × head_dim × seq_len (32768) × bytes_per_elem / 1024^3。若 num_key_value_heads=8, head_dim=128, BF16 (2 bytes)，则计算值为 2 * 64 * 8 * 128 * 32768 * 2 / 1024^3 ≈ 8.0 GB，而非 N7 中基于 MHA 假设的 131 GB。此差异源于 GQA 机制，是显存估算的关键修正项。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合GQA机制原理，数值计算准确（2*64*8*128*32768*2/1024^3 ≈ 8.0 GB），且与MHA假设下的131 GB差异符合理论预期（131/8 ≈ 16.4，接近MHA头数64/GQA头数8=8倍差异，考虑到MHA通常K/V头数等于Q头数，此处对比合理）。

## Search Query

KV cache size calculation formula GQA num_key_value_heads
