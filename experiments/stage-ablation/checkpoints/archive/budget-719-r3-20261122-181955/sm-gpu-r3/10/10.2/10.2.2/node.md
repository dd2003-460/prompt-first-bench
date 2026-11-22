# N370: 基于修正后的参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），32K上下文下单请求KV Cache占用 =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

基于修正后的参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），32K上下文下单请求KV Cache占用 = 256 KB/token * 32768 tokens = 8 GB。A100 80GB在BF16权重(54GB)下剩余显存 = 80 - 54 = 26 GB，可支持并发请求数 = 26 GB / 8 GB = 3.25，即最大3个并发请求（保留1GB系统余量后为2个）。

## Corrected Claim

基于修正后的参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），32K上下文下单请求KV Cache占用 = 256 KB/token * 32768 tokens = 8 GB。A100 80GB在BF16权重(54GB)下剩余显存 = 80 - 54 = 26 GB，可支持并发请求数 = 26 GB / 8 GB = 3.25，即最大3个并发请求（保留1GB系统余量后为2个）。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache计算 (2 * 8 * 64 * 128 * 2 bytes) * 32768 = 8GB 正确；显存余量 80-54=26GB 正确；并发数 26/8=3.25 取整为3（或保留余量后为2）逻辑自洽。
