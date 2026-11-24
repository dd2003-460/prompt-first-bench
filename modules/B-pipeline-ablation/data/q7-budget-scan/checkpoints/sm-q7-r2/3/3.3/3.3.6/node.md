# N62: HDD 阵列重建期间额外电力成本 = (重建时长小时 × 单盘功耗W × 盘数 × 电价¥/kWh)，其中重建时长取 24 小时（RAID6 典型值），单盘功耗

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14, N15, N16

## Claim

HDD 阵列重建期间额外电力成本 = (重建时长小时 × 单盘功耗W × 盘数 × 电价¥/kWh)，其中重建时长取 24 小时（RAID6 典型值），单盘功耗取 7W，电价取 ¥0.8/kWh，需乘以故障频率（盘数 × AFR）得到年均值。

## Corrected Claim

HDD 阵列重建期间额外电力成本 = (重建时长小时 × 单盘功耗W × 盘数 × 电价¥/kWh)，其中重建时长取 24 小时（RAID6 典型值），单盘功耗取 7W，电价取 ¥0.8/kWh，需乘以故障频率（盘数 × AFR）得到年均值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HDD RAID rebuild time power consumption
