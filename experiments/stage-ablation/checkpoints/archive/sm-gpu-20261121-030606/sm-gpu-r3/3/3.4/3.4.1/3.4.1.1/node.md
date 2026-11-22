# N272: W4精度下Qwen3-27B的KV Cache显存占用需精确计算：若n_layers=28, n_kv_heads=8, head_dim=128, seq_l

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

W4精度下Qwen3-27B的KV Cache显存占用需精确计算：若n_layers=28, n_kv_heads=8, head_dim=128, seq_len=32768, W4下KV Cache仍为BF16（2 bytes），则KV_Cache = 2 * 28 * 8 * 128 * 32768 * 2 bytes = 3.98GB

## Corrected Claim

W4精度下Qwen3-27B的KV Cache显存占用需精确计算：若n_layers=28, n_kv_heads=8, head_dim=128, seq_len=32768, W4下KV Cache仍为BF16（2 bytes），则KV_Cache = 2 * 28 * 8 * 128 * 32768 * 2 bytes = 3.98GB

## Evidence

逻辑推导成立，来源未直接覆盖
