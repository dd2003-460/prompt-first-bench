# N44: RTX 4090 单卡/双卡/四卡配置下的峰值功耗分别为 450W/900W/1800W，基于 TDP 1.5倍冗余系数计算，所需电源瓦数下限为 675W/13

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

RTX 4090 单卡/双卡/四卡配置下的峰值功耗分别为 450W/900W/1800W，基于 TDP 1.5倍冗余系数计算，所需电源瓦数下限为 675W/1350W/2700W。

## Corrected Claim

RTX 4090 单卡/双卡/四卡配置下的峰值功耗分别为 450W/900W/1800W，基于 TDP 1.5倍冗余系数计算，所需电源瓦数下限为 675W/1350W/2700W。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 为 450W，线性叠加及 1.5 倍冗余系数计算（450*1.5=675, 900*1.5=1350, 1800*1.5=2700）在数学和工程逻辑上自洽。

## Search Query

RTX 4090 TDP power consumption multi-GPU PSU requirement
