# N754: MI300X 运行 Qwen3-27B 的 BF16 权重内存占用精确值为 54.0 GB (27B 参数 * 2 bytes)，占 192GB HBM3 总容

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N233, N234, N235

## Claim

MI300X 运行 Qwen3-27B 的 BF16 权重内存占用精确值为 54.0 GB (27B 参数 * 2 bytes)，占 192GB HBM3 总容量的 28.125%，剩余可用显存为 138.0 GB，足以容纳 32K 上下文下的 KV Cache 及激活值缓冲。

## Corrected Claim

MI300X 运行 Qwen3-27B 的 BF16 权重内存占用精确值为 54.0 GB (27B 参数 * 2 bytes)，占 192GB HBM3 总容量的 28.125%，剩余可用显存为 138.0 GB，足以容纳 32K 上下文下的 KV Cache 及激活值缓冲。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 2 bytes = 54GB，54/192 = 28.125%，192-54=138GB，计算完全自洽且符合MI300X硬件规格常识。
