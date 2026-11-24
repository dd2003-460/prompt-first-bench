# N358: 平均 RPS 高负载工作点：RPS_avg_high = 1,666,667 / 86,400 ≈ 19.29 RPS，对应 s=1.2MB 的低对象大小场景，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

平均 RPS 高负载工作点：RPS_avg_high = 1,666,667 / 86,400 ≈ 19.29 RPS，对应 s=1.2MB 的低对象大小场景，可能触发公有云 CDN 流量包超额计费

## Corrected Claim

平均 RPS 高负载工作点：RPS_avg_high = 1,666,667 / 86,400 ≈ 19.29 RPS，对应 s=1.2MB 的低对象大小场景，可能触发公有云 CDN 流量包超额计费

## Evidence

先验知识/题面给定，逻辑校验通过：1,666,667 / 86,400 ≈ 19.29 计算正确，量级合理，符合低对象大小高并发场景特征。
