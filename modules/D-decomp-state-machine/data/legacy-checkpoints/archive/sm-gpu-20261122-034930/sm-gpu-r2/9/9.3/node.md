# N147: 2x RTX 4090 (NVLink/PCIe) 在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的有效吞吐率受限于PCIe 4

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N43

## Claim

2x RTX 4090 (NVLink/PCIe) 在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的有效吞吐率受限于PCIe 4.0 x16带宽(64GB/s)对KV Cache分片同步的瓶颈，理论上限约为 min(单卡带宽/2, PCIe带宽) ≈ 32 tokens/s，显著低于A100单卡的54.1 tokens/s。

## Corrected Claim

2x RTX 4090 (PCIe互联) 在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的有效吞吐率可能受限于PCIe 4.0 x16带宽对KV Cache分片同步的瓶颈，具体数值需依赖实际基准测试，但通常显著低于A100单卡性能。

## Evidence

[质询]该陈述包含多个具体的经验性硬件参数和性能数值（如PCIe 4.0 x16带宽64GB/s、A100单卡54.1 tokens/s、RTX 4090双卡32 tokens/s），这些属于经验事实，无法仅从第一性原理严格推导。此外，'NVLink/PCIe'表述模糊，RTX 4090不支持NVLink，若指PCIe互联，其KV Cache同步瓶颈的具体量化（32 tokens/s）缺乏通用理论支持，可能依赖于特定软件栈或实现细节，存在数值不准确或过度简化的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

2x RTX 4090 PCIe bottleneck LLM inference throughput
