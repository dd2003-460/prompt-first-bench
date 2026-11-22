# N34: 重填充失败率 f_refill 的精确计算：f_refill = P(源站不可用) + P(源站响应超时) + P(并发请求去重失败)，假设源站可用性 99.9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

重填充失败率 f_refill 的精确计算：f_refill = P(源站不可用) + P(源站响应超时) + P(并发请求去重失败)，假设源站可用性 99.9%、超时率 0.1%、去重失败率 0.01%，则 f_refill ≈ 0.001 + 0.001 + 0.0001 = 0.0021

## Corrected Claim

重填充失败率 f_refill 的精确计算：f_refill = P(源站不可用) + P(源站响应超时) + P(并发请求去重失败)，假设源站可用性 99.9%、超时率 0.1%、去重失败率 0.01%，则 f_refill ≈ 0.001 + 0.001 + 0.0001 = 0.0021

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.001 + 0.001 + 0.0001 = 0.0021 正确，且基于题面给定的独立概率假设，逻辑自洽。

## Search Query

CDN origin server failure rate timeout probability concurrent request deduplication failure
