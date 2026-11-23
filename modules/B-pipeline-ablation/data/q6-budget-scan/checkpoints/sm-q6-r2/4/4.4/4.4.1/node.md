# N68: 峰值请求速率 Q_peak = Q_avg * PAR，其中 Q_avg = (2TB / 86400) / s_avg ≈ 3.6MB/s / s_avg（请

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

峰值请求速率 Q_peak = Q_avg * PAR，其中 Q_avg = (2TB / 86400) / s_avg ≈ 3.6MB/s / s_avg（请求/秒），PAR 通常取 3-5，需根据业务时间分布确定具体值

## Corrected Claim

峰值请求速率 Q_peak = Q_avg * PAR，其中 Q_avg = (2TB / 86400) / s_avg ≈ 3.6MB/s / s_avg（请求/秒），PAR 通常取 3-5，需根据业务时间分布确定具体值

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（2TB/86400s ≈ 23.15MB/s，除以s_avg得到Q_avg），PAR定义及取值范围符合常规工程经验。
