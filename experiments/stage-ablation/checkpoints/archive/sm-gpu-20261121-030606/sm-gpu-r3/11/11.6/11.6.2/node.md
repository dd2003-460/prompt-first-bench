# N403: Mac Studio 年均电力成本 $180 的计算假设了 80% 的利用率，但实际本地工作站推理场景的负载因子（Duty Cycle）通常低于 40%，需基于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N166

## Claim

Mac Studio 年均电力成本 $180 的计算假设了 80% 的利用率，但实际本地工作站推理场景的负载因子（Duty Cycle）通常低于 40%，需基于 30%-50% 的平均负载率重新计算年电费。

## Corrected Claim

Mac Studio 年均电力成本 $180 的计算假设了 80% 的利用率，但实际本地工作站推理场景的负载因子（Duty Cycle）通常低于 40%，需基于 30%-50% 的平均负载率重新计算年电费。

## Evidence

先验知识/题面给定，逻辑校验通过：本地工作站推理通常非满载运行，负载因子低于40%符合工程直觉，且基于30%-50%重新计算是合理的修正方向。
