# N156: 工作点 B (动态更新干扰)：当更新率 1%/天 时，LFU 频率计数器老化，对新兴热点响应滞后，ΔH_byte 显著缩小，甚至可能因缓存陈旧对象而低于 LRU

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点 B (动态更新干扰)：当更新率 1%/天 时，LFU 频率计数器老化，对新兴热点响应滞后，ΔH_byte 显著缩小，甚至可能因缓存陈旧对象而低于 LRU，增益上限需乘以衰减因子 e^(-λ_update * τ_lag)。

## Corrected Claim

工作点 B (动态更新干扰)：当更新率 1%/天 时，LFU 频率计数器老化，对新兴热点响应滞后，ΔH_byte 显著缩小，甚至可能因缓存陈旧对象而低于 LRU，增益上限需乘以衰减因子 e^(-λ_update * τ_lag)。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 基于历史频率，在动态更新场景下确实存在计数器老化导致对新兴热点响应滞后的问题，且引入衰减因子 e^(-λ_update * τ_lag) 符合指数衰减模型的基本逻辑，量纲与物理直觉自洽。
