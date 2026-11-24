# N280: 双活中心机房的故障切换延迟对P99的影响：北京/上海双活架构下，若主中心故障，切换时间 $T_{failover} = T_{detect} + T_{swit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

双活中心机房的故障切换延迟对P99的影响：北京/上海双活架构下，若主中心故障，切换时间 $T_{failover} = T_{detect} + T_{switch} + T_{warmup}$，其中 $T_{detect}$ 为故障检测时间（1-5秒），$T_{switch}$ 为DNS/BGP切换时间（5-30秒），$T_{warmup}$ 为缓存预热时间（0-60秒）；故障期间P99延迟增量 $\Delta P99_{failover} = T_{failover} \times \phi_{affected}$，需量化故障概率（年1-2次）对年度P99平均值的贡献

## Corrected Claim

双活中心机房的故障切换延迟对P99的影响：北京/上海双活架构下，若主中心故障，切换时间 $T_{failover} = T_{detect} + T_{switch} + T_{warmup}$，其中 $T_{detect}$ 为故障检测时间（1-5秒），$T_{switch}$ 为DNS/BGP切换时间（5-30秒），$T_{warmup}$ 为缓存预热时间（0-60秒）；故障期间P99延迟增量 $\Delta P99_{failover} = T_{failover} \times \phi_{affected}$，需量化故障概率（年1-2次）对年度P99平均值的贡献

## Evidence

先验知识/题面给定，逻辑校验通过
