# N43: miss 成本 cost_miss(s) 的函数：cost_miss(s) = t_refill(s) + t_processing，t_processing 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

miss 成本 cost_miss(s) 的函数：cost_miss(s) = t_refill(s) + t_processing，t_processing = 1ms，cost_miss(s) = 6ms + s/100MB/s

## Corrected Claim

miss 成本 cost_miss(s) 的函数：cost_miss(s) = t_refill(s) + t_processing，t_processing = 1ms，cost_miss(s) = 6ms + s/100MB/s

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合缓存缺失成本定义（重填时间+处理时间），数值量级（6ms重填+1ms处理）在常规系统模拟中合理，且source为knowledge，无需外部来源支持。

## Search Query

cache miss cost function processing time refill latency
