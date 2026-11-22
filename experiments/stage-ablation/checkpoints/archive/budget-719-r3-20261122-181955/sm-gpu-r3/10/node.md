# N37: 2x RTX 4090 (PCIe 4.0 x16) 进行 TP=2 推理时，由于 PCIe 带宽限制 (64 GB/s) 远高于 NVLink (900 GB

- **status**: pending
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

父节点级核验未通过：不完备（子节点1聚焦于双卡PCIe互联的通信瓶颈，子节点2聚焦于单卡显存容量对并发数的限制，两者主题正交且不重复。但父节点明确提到了'2x RTX 4090'作为整体系统，子节点2仅分析了单张RTX 4090的KV Cache容量，未涵盖双卡总显存（48GB）对系统整体并发能力的贡献，导致对父节点中'RTX 4090系统'的并发能力描述不完整。）
