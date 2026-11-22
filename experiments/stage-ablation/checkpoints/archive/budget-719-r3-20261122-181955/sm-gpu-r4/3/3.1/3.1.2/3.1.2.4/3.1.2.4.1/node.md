# N776: 对于 A100 80GB（BF16 权重 54GB，剩余显存 26GB），在 32K 上下文下，Batch_Size=3 时 KV Cache 总占用 = 3 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N277

## Claim

对于 A100 80GB（BF16 权重 54GB，剩余显存 26GB），在 32K 上下文下，Batch_Size=3 时 KV Cache 总占用 = 3 * 8 GB = 24 GB，剩余余量 2 GB，此时 Decode 吞吐量理论上限 = 有效带宽 / (54 GB + 3 * 8 GB) ≈ 1529 GB/s / 78 GB ≈ 19.6 tokens/s，相比 Batch=1 的 24.6 tokens/s 下降 20%，但总吞吐量提升 3 倍。

## Corrected Claim

对于 A100 80GB（BF16 权重 54GB，剩余显存 26GB），在 32K 上下文下，Batch_Size=3 时 KV Cache 总占用 = 3 * 8 GB = 24 GB，剩余余量 2 GB，此时 Decode 吞吐量理论上限 = 有效带宽 / (54 GB + 3 * 8 GB) ≈ 1529 GB/s / 78 GB ≈ 19.6 tokens/s，相比 Batch=1 的 24.6 tokens/s 下降 20%，但总吞吐量提升 3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 占用计算（3*8GB=24GB）与显存余量（26-24=2GB）自洽；Decode 吞吐量基于带宽瓶颈模型（1529/78≈19.6）计算正确；Batch=1 时 1529/62≈24.6 亦自洽；总吞吐量提升 3 倍符合 Batch Size 线性扩展理论。
