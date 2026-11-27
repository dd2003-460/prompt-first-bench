# N335: 在 W4 单卡工作点下，RX 7900 XTX 无需多卡通信，规避了 PCIe 瓶颈；其 14GB 显存占用允许在 32K 上下文下保留完整的 KV Cache

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

在 W4 单卡工作点下，RX 7900 XTX 无需多卡通信，规避了 PCIe 瓶颈；其 14GB 显存占用允许在 32K 上下文下保留完整的 KV Cache，理论 Decode TPS 受限于 1008GB/s 带宽与 SM 效率，预计可达 40-50 tokens/s [待核验]，无 AllReduce 开销。

## Corrected Claim

在 W4 单卡工作点下，RX 7900 XTX 无需多卡通信，规避了 PCIe 瓶颈；其显存占用（约 14GB）允许在 32K 上下文下保留完整的 KV Cache，理论 Decode TPS 受限于 1008GB/s 带宽与 SM 效率，预计可达数十 tokens/s，无 AllReduce 开销。

## Evidence

[质询]数值量级与硬件规格存在潜在矛盾：RX 7900 XTX 显存为 24GB 而非 14GB（14GB 可能是特定模型权重+KV Cache 的占用量，但表述易混淆）；且 40-50 tokens/s 的 Decode TPS 在 1008GB/s 带宽下对于大模型（如 7B+）可能偏高或偏低，取决于具体模型大小和量化方式，缺乏具体模型上下文导致数值难以精确验证。 | 先验知识/题面给定，逻辑校验通过：单卡无 AllReduce 开销逻辑正确；RX 7900 XTX 带宽 1008GB/s 符合规格；但 14GB 显存占用与 24GB 总显存的表述需澄清，且 TPS 数值依赖具体模型，故降级为定性表述。
