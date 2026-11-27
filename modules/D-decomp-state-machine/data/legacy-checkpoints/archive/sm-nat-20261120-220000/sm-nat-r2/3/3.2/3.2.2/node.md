# N38: 请求间隔 t_request 的分布：基于泊松过程，t_request ~ Exponential(λ=5000万/天 ≈ 578.7 req/s)，平均 t_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

请求间隔 t_request 的分布：基于泊松过程，t_request ~ Exponential(λ=5000万/天 ≈ 578.7 req/s)，平均 t_request ≈ 1.73ms

## Corrected Claim

请求间隔 t_request 的分布：基于泊松过程，t_request ~ Exponential(λ=5000万/天 ≈ 578.7 req/s)，平均 t_request ≈ 1.73ms

## Evidence

先验知识/题面给定，逻辑校验通过：5000万/天换算为秒级速率约为 578.7 req/s，其倒数即为平均间隔 1.73ms，数学推导自洽。

## Search Query

Poisson process request interarrival time CDN traffic rate
