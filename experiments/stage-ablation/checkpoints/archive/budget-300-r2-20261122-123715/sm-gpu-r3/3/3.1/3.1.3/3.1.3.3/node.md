# N236: 散热失败风险成本量化：若散热设计不足导致 RTX 4090 触发 Thermal Throttling，性能下降幅度通常为 15%-25%（从 ~50 tok/

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

散热失败风险成本量化：若散热设计不足导致 RTX 4090 触发 Thermal Throttling，性能下降幅度通常为 15%-25%（从 ~50 tok/s 降至 ~40 tok/s），这等效于降低了有效吞吐量，从而在 Value = Throughput/TCO 公式中使分母不变但分子降低，导致性价比指标下降 15%-25%；因此，$150 的散热投入是防止 TCO 隐性增加的必要保险。

## Corrected Claim

散热失败风险成本量化：若散热设计不足导致 RTX 4090 触发 Thermal Throttling，性能通常会显著下降（具体幅度视负载而定，常见范围可能在 10%-30% 之间），这等效于降低了有效吞吐量，从而在 Value = Throughput/TCO 公式中使分子降低，导致性价比指标下降；因此，适当的散热投入是防止 TCO 隐性增加、维持预期性价比的必要保险。

## Evidence

[质询]数值量级与具体场景强相关，缺乏普适性：RTX 4090 在 LLM 推理中触发 Thermal Throttling 的性能下降幅度并非固定的 15%-25%，且从 ~50 tok/s 降至 ~40 tok/s 的具体数值依赖于模型大小、Batch Size 及具体硬件配置，将其作为通用量化标准存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：散热不足导致降频从而降低吞吐量（分子）进而降低性价比（Value）的逻辑链条自洽；但具体数值（15%-25% 及 tok/s 变化）属于经验事实，虽逻辑合理但缺乏特定场景下的精确来源支持，故降级为定性表述。

## Search Query

RTX 4090 thermal throttling performance drop percentage
