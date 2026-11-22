# N179: H200 剩余 74.42GB 显存用于 KV Cache 扩展时，若保持 BF16 精度，最大支持上下文长度 = 74.42GB / (12.58GB / 3

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

H200 剩余 74.42GB 显存用于 KV Cache 扩展时，若保持 BF16 精度，最大支持上下文长度 = 74.42GB / (12.58GB / 32K) ≈ 189.5K tokens；若启用 FP8 KV Cache (6.29GB/32K)，最大支持上下文长度 = 74.42GB / (6.29GB / 32K) ≈ 379K tokens，突破 128K 限制的关键在于 KV Cache 量化而非仅依赖容量。

## Corrected Claim

H200 剩余 74.42GB 显存用于 KV Cache 扩展时，若保持 BF16 精度，最大支持上下文长度 = 74.42GB / (12.58GB / 32K) ≈ 189.5K tokens；若启用 FP8 KV Cache (6.29GB/32K)，最大支持上下文长度 = 74.42GB / (6.29GB / 32K) ≈ 379K tokens，突破 128K 限制的关键在于 KV Cache 量化而非仅依赖容量。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点存在严重数据错误（KV Cache 计算量级错误，导致结论与父节点矛盾）；且子节点2和3本质上是同一计算逻辑在不同精度下的参数实例，具有高度冗余性。）
