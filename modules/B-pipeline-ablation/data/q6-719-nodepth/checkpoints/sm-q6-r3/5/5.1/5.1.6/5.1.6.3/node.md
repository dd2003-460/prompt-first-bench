# N315: 过载丢弃率 D_overload 对 P99 延迟的具体影响量化：当 D_overload > 0 时，P99 延迟不再遵循常规分布，而是由重试机制决定。假设重

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

过载丢弃率 D_overload 对 P99 延迟的具体影响量化：当 D_overload > 0 时，P99 延迟不再遵循常规分布，而是由重试机制决定。假设重试率为 50%，重试间隔为 100ms，则 P99_latency_overload ≈ T_normal + 0.5 × (100ms + T_normal_retry)，其中 T_normal_retry 为重试后的正常延迟。

## Corrected Claim

过载丢弃率 D_overload > 0 时，P99 延迟显著偏离常规分布，主要受重试机制影响。在简化模型下，若重试率为 50%，重试间隔为 100ms，P99 延迟可近似估算为 T_normal + 0.5 × (100ms + T_normal_retry)，但实际值可能因重试风暴和排队效应而更高。

## Evidence

[质询]该公式将P99延迟简化为线性加权平均，忽略了重试机制对尾部延迟的非线性放大效应（如重试风暴导致的排队延迟激增）以及P99统计量本身的非线性特性，属于过度简化的经验模型而非严格推导。 | 先验知识/题面给定，逻辑校验通过（量纲一致，公式结构合理），但作为经验事实缺乏来源直接支持，且模型简化程度较高，故降级为定性表述。
