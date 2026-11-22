# N252: RTX 4090 在 Qwen3-27B BF16 权重场景下，因 24GB 显存不足无法单卡运行，必须采用 2x 4090 方案；此时总有效带宽受限于 PCI

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

RTX 4090 在 Qwen3-27B BF16 权重场景下，因 24GB 显存不足无法单卡运行，必须采用 2x 4090 方案；此时总有效带宽受限于 PCIe 4.0 x16 互联带宽 (32 GB/s) 及 NVLink 缺失导致的 P2P 通信开销，实际聚合 Decode 速度上限约为 (1008 * 2 * 0.75 - C_comm) / 56GB ≈ 25-30 tokens/s，远低于单卡 INT4 方案。

## Corrected Claim

RTX 4090 在 Qwen3-27B BF16 权重场景下，因 24GB 显存不足无法单卡运行，必须采用 2x 4090 方案；此时总有效带宽受限于 PCIe 4.0 x16 互联带宽（单向约 32 GB/s，双向约 64 GB/s）及缺乏高速互联（如 NVLink）导致的 P2P 通信开销（通常经 CPU 或 PCIe 交换），实际聚合 Decode 速度上限约为 25-30 tokens/s（具体取决于批处理大小和序列长度），远低于单卡 INT4 方案。

## Evidence

[质询]RTX 4090 不支持 NVLink，因此陈述中提到的 'NVLink 缺失导致的 P2P 通信开销' 在技术实现上存在误导（通常指 PCIe P2P 或 CPU 中转开销，而非 NVLink 缺失本身产生的特定开销类型，且 PCIe 4.0 x16 双向带宽约为 64GB/s，单向 32GB/s，聚合带宽计算需考虑具体通信模式，此处简化为 32GB/s 可能低估或高估实际瓶颈，取决于是否双向同时传输）。此外，Qwen3-27B BF16 权重约为 54GB，确实无法在单张 24GB 卡上运行，但 2x 4090 通过 PCIe 互联的 Decode 速度受限于内存带宽和通信延迟，25-30 tokens/s 的估算依赖于具体的批处理大小和序列长度，缺乏具体上下文时该数值范围可能偏乐观或悲观。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 无 NVLink 是事实，24GB 显存无法容纳 27B BF16 模型（~54GB）是事实，PCIe 4.0 x16 带宽限制是事实。但具体速度估算 25-30 tokens/s 为经验性推导，缺乏精确来源支持，且 'NVLink 缺失导致的 P2P 通信开销' 表述略显不严谨（应为 PCIe P2P 或 CPU 中转开销），故降级为 degraded。

## Search Query

2x RTX 4090 tensor parallel LLM inference throughput penalty PCIe vs NVLink
