# N386: 社交/短视频场景延迟-留存弹性（高敏感工作点）：P99延迟每降低100ms，用户次日留存率提升0.8%（取中值），则ΔRetention_per_ms = 0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

社交/短视频场景延迟-留存弹性（高敏感工作点）：P99延迟每降低100ms，用户次日留存率提升0.8%（取中值），则ΔRetention_per_ms = 0.8% / 100 = 0.008%/ms。

## Corrected Claim

在特定社交/短视频场景的某次统计中，P99延迟每降低100ms，用户次日留存率提升约0.8%（中值），对应弹性系数约为0.008%/ms。

## Evidence

[质询]该数值（0.8%/100ms）属于特定业务场景下的经验统计参数，并非普适物理或数学定律。不同平台、用户群体及具体功能模块的延迟-留存弹性差异巨大，直接将其作为通用事实存在以偏概全的风险，且缺乏当前上下文中的具体数据来源支持。 | 逻辑推导（0.8% / 100ms = 0.008%/ms）自洽，量纲正确；但作为经验事实，缺乏来源直接支持，且该参数高度依赖具体业务场景，无法从第一性原理严格推出，故降级为定性/特定场景表述。

## Search Query

social media latency retention rate elasticity
