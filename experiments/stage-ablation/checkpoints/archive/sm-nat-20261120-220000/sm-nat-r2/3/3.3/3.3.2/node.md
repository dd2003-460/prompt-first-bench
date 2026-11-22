# N42: 重填充成本 cost_refill(s) 的函数：cost_refill(s) = t_refill_base + s / bandwidth，t_refill

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

重填充成本 cost_refill(s) 的函数：cost_refill(s) = t_refill_base + s / bandwidth，t_refill_base = 5ms，bandwidth = 100MB/s，cost_refill(s) = 5ms + s/100MB/s

## Corrected Claim

重填充成本 cost_refill(s) 的函数：cost_refill(s) = t_refill_base + s / bandwidth，t_refill_base = 5ms，bandwidth = 100MB/s，cost_refill(s) = 5ms + s/100MB/s

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache refill cost function object size bandwidth latency
