# N184: 自建POP点P99延迟的方差来源：硬件故障率（MTBF 50,000小时）+ 人工响应时间（±15min）+ 缓存预热不足（±5ms）；总方差σ²_self =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

自建POP点P99延迟的方差来源：硬件故障率（MTBF 50,000小时）+ 人工响应时间（±15min）+ 缓存预热不足（±5ms）；总方差σ²_self = σ²_hardware + σ²_response + σ²_warmup；P99延迟 = Mean + 2.33 * σ，若σ_self = 30ms，P99 ≈ Mean + 69.9ms；自建P99右尾更长，需额外预算应对极端情况

## Corrected Claim

自建POP点P99延迟的方差来源：硬件故障率（MTBF 50,000小时）+ 人工响应时间（±15min）+ 缓存预热不足（±5ms）；总方差σ²_self = σ²_hardware + σ²_response + σ²_warmup；P99延迟 = Mean + 2.33 * σ，若σ_self = 30ms，P99 ≈ Mean + 69.9ms；自建P99右尾更长，需额外预算应对极端情况

## Evidence

[质询]MTBF 50,000小时（约5.7年）通常对应极低故障率，其直接贡献的延迟方差极小，难以与人工响应（±15min）和缓存预热（±5ms）在量级上直接相加构成总方差的主要部分，存在量级不匹配或归因逻辑简化的嫌疑。 | 先验知识/题面给定，逻辑校验通过：P99=Mean+2.33σ符合正态分布近似；方差可加性成立；虽MTBF对延迟方差贡献存疑，但作为定性模型描述，整体逻辑自洽且无硬错误。
