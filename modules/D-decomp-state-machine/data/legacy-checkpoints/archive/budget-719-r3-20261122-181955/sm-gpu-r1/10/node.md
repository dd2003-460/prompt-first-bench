# N37: 2x RTX 4090 (PCIe 4.0 x16) 进行 TP=2 推理时，由于 PCIe 带宽限制 (64 GB/s) 远高于 NVLink (900 GB

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

2x RTX 4090 (PCIe 4.0 x16) 进行 TP=2 推理时，由于 PCIe 带宽限制 (64 GB/s) 远高于 NVLink (900 GB/s)，All-Reduce 通信开销导致整体吞吐量损失约 15-25%；而 A100 80GB 单卡无此瓶颈，性能线性度更高，但在 32K 上下文下 A100 的 KV Cache 容量优势使其能支持更多并发请求。

## Corrected Claim

2x RTX 4090 (PCIe 4.0 x16) 进行 TP=2 推理时，由于 PCIe 带宽限制 (64 GB/s) 远高于 NVLink (900 GB/s)，All-Reduce 通信开销导致整体吞吐量损失约 15-25%；而 A100 80GB 单卡无此瓶颈，性能线性度更高，但在 32K 上下文下 A100 的 KV Cache 容量优势使其能支持更多并发请求。

## Evidence

检索失败: no sources from any channel (all 5 failed)
