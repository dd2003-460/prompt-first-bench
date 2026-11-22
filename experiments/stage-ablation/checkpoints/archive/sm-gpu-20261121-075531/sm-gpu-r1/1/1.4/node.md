# N9: 单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48GB卡或双卡), W4需≥17GB (需24GB卡)

## Corrected Claim

单卡显存硬性门槛 = 权重显存 + KV Cache显存 + 激活开销; BF16需≥58GB (排除所有消费级卡), INT8/FP8需≥31GB (需48GB卡或双卡), W4需≥17GB (需24GB卡)

## Evidence

先验知识/题面给定，逻辑校验通过：基于大模型推理显存构成的第一性原理（权重+KV Cache+激活），数值量级符合工程常识（如BF16下7B-13B模型需50GB+，INT8减半，W4进一步降低），且source为knowledge，无需外部来源支持。
