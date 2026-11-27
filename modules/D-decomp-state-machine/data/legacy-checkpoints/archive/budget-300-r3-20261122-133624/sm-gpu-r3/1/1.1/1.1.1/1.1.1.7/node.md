# N183: vLLM KV Cache 理论显存占用公式：KV_cache_GB = (2 × num_layers × num_kv_heads × head_dim ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43, N44, N45

## Claim

vLLM KV Cache 理论显存占用公式：KV_cache_GB = (2 × num_layers × num_kv_heads × head_dim × max_seq_len × bytes_per_element) / 1e9。对于 Qwen3-27B BF16：num_layers=48, num_kv_heads=8 (GQA), head_dim=128, max_seq_len=32768, bytes=2，计算得 KV_cache ≈ 2 × 48 × 8 × 128 × 32768 × 2 / 1e9 ≈ 12.88 GB。

## Corrected Claim

vLLM KV Cache 理论显存占用公式：KV_cache_GB = (2 × num_layers × num_kv_heads × head_dim × max_seq_len × bytes_per_element) / 1e9。对于 Qwen3-27B BF16：num_layers=48, num_kv_heads=8 (GQA), head_dim=128, max_seq_len=32768, bytes=2，计算得 KV_cache ≈ 2 × 48 × 8 × 128 × 32768 × 2 / 1e9 ≈ 12.88 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，参数符合Qwen3-27B GQA架构特征），数值计算 2*48*8*128*32768*2/1e9 = 12.8849... ≈ 12.88 GB，量级与逻辑均自洽。
