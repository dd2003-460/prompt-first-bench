# N60: 消费级双卡方案 (2x RTX 4090) 的互联瓶颈成本项：PCIe 4.0 x16 理论带宽 32GB/s，实际有效带宽受 x8/x8 物理限制降至 ~16

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

消费级双卡方案 (2x RTX 4090) 的互联瓶颈成本项：PCIe 4.0 x16 理论带宽 32GB/s，实际有效带宽受 x8/x8 物理限制降至 ~16GB/s，导致 KV Cache 跨卡传输延迟增加 ~15-20ms/token，需通过 CPU RAM Offload 补偿，额外增加 ~50-100GB DDR5 内存成本 ($200-$400) 及主板/CPU 平台溢价 ($800-$1200)。

## Corrected Claim

消费级双卡方案 (2x RTX 4090) 受限于 PCIe 4.0 x8/x8 物理拓扑，有效互联带宽降至约 16GB/s，显著增加 KV Cache 跨卡传输开销；为缓解此瓶颈，通常需依赖 CPU RAM Offload，这将引入额外的 DDR5 内存需求（数十至百 GB 级别）及相应的主板/CPU 平台成本溢价。

## Evidence

[质询]KV Cache 跨卡传输延迟的具体数值（~15-20ms/token）缺乏明确的上下文依赖（如序列长度、Batch Size、模型架构），且该延迟量级对于 PCIe 4.0 x8 (~16GB/s) 带宽而言，仅在特定大模型长序列场景下才可能成立，作为通用陈述存在数值量级不确定的风险；此外，CPU RAM Offload 的成本估算（$200-$400 for 50-100GB DDR5）在当前市场波动下可能偏低，且将硬件成本与性能瓶颈直接挂钩的逻辑链条较为复杂，容易混淆因果关系。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 32GB/s 及 x8/x8 分叉后约 16GB/s 的物理限制符合硬件规范；虽然具体延迟和成本为经验估计且无外部来源支持，但整体技术逻辑（带宽瓶颈导致通信开销，需通过内存卸载补偿并增加硬件成本）自洽，故降级为定性表述以规避具体数值的潜在偏差。

## Search Query

RTX 4090 dual card PCIe bandwidth bottleneck latency vLLM
