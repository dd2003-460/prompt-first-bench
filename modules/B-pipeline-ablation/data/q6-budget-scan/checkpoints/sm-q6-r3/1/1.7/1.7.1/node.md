# N69: T_cache_hit_P99_self = max_i (RTT_P99(i) + T_proc_P99(i) + T_queue_P99(i))，其中i遍历

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_cache_hit_P99_self = max_i (RTT_P99(i) + T_proc_P99(i) + T_queue_P99(i))，其中i遍历10个POP点，需计算各点独立P99后取最大值，而非平均

## Corrected Claim

T_cache_hit_P99_self = max_i (RTT_P99(i) + T_proc_P99(i) + T_queue_P99(i))，其中i遍历10个POP点，需计算各点独立P99后取最大值，而非平均

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟通常定义为最坏情况下的独立组件延迟之和，取最大值符合保守估计原则，量纲与逻辑自洽。
