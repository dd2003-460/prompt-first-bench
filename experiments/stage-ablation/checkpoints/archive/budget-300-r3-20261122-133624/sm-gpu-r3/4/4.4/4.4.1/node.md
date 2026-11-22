# N106: RTX 4090 在持续高负载（>90% GPU Utilization）下的热降频阈值：当显存温度超过 90°C 或核心温度超过 83°C 时，NVIDIA 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

RTX 4090 在持续高负载（>90% GPU Utilization）下的热降频阈值：当显存温度超过 90°C 或核心温度超过 83°C 时，NVIDIA 驱动会强制降低时钟频率 5-10%，导致 Decode 吞吐量波动范围扩大至 ±15%，影响长上下文生成的稳定性。

## Corrected Claim

RTX 4090 在持续高负载下，当显存或核心温度超过特定阈值（通常随驱动版本和散热条件变化，常见参考值约为显存90°C/核心83°C）时，NVIDIA 驱动会触发热降频机制，导致时钟频率降低，进而引起 Decode 吞吐量波动，影响长上下文生成的稳定性。

## Evidence

[质询]具体数值阈值（90°C/83°C）及性能波动幅度（±15%）缺乏通用标准支持，不同驱动版本、散热条件及具体负载类型下，NVIDIA的降频策略和实际性能衰减表现存在显著差异，将特定经验值表述为固定事实存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过（热降频机制符合物理直觉，量级合理），但具体参数值属于经验事实且无外部来源直接支持，故降级。

## Search Query

RTX 4090 thermal throttling temperature limit sustained load
