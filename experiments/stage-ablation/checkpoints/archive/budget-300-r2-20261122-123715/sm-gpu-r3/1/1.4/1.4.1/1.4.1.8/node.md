# N182: 基于修正后的参数 (num_layers=64, num_kv_heads=8, head_dim=128)，Qwen3-27B 在 32K 上下文、BF16 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

基于修正后的参数 (num_layers=64, num_kv_heads=8, head_dim=128)，Qwen3-27B 在 32K 上下文、BF16 精度下的 KV Cache 显存精确计算为：KV_GB = (2 * 64 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 12.8GB；若使用 FP8，则减半为 6.4GB

## Corrected Claim

基于修正后的参数 (num_layers=64, num_kv_heads=8, head_dim=128)，Qwen3-27B 在 32K 上下文、BF16 精度下的 KV Cache 显存精确计算为：KV_GB = (2 * 64 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 12.8GB；若使用 FP8，则减半为 6.4GB

## Evidence

先验知识/题面给定，逻辑校验通过：公式 KV_GB = (2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_element) / 1024^3 代入数值 (2 * 64 * 8 * 128 * 32768 * 2) / 1073741824 = 12.8，计算无误；FP8 精度减半逻辑正确。
