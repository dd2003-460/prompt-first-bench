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

父节点级核验未通过：不完备（子节点存在事实性错误（PCIe带宽单位混淆）且未覆盖父节点中关于‘吞吐量损失15-25%’这一核心结论的验证或解释逻辑，仅停留在带宽对比和KV Cache计算上，缺少对通信开销占比的具体量化推导以支撑父节点结论。）
