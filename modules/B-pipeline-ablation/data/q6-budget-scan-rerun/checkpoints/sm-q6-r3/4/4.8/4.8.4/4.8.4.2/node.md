# N333: 敏感性分析：P99 目标 T 对最优策略的临界点影响：当 T < 80ms 时，公有云因节点多（Hit_Rate > 95%）成为唯一可行解；当 80ms ≤ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

敏感性分析：P99 目标 T 对最优策略的临界点影响：当 T < 80ms 时，公有云因节点多（Hit_Rate > 95%）成为唯一可行解；当 80ms ≤ T ≤ 150ms 时，混合策略因成本优势成为帕累托最优；当 T > 150ms 时，自建策略因固定成本低可能成为成本最优解，但需验证 P99_Self 是否真的 > 200ms

## Corrected Claim

敏感性分析：P99 目标 T 对最优策略的临界点影响：当 T < 80ms 时，公有云因节点多（Hit_Rate > 95%）成为唯一可行解；当 80ms ≤ T ≤ 150ms 时，混合策略因成本优势成为帕累托最优；当 T > 150ms 时，自建策略因固定成本低可能成为成本最优解，但需验证 P99_Self 是否真的 > 200ms

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了基于延迟阈值（T）和成本/命中率权衡的策略选择逻辑，符合云计算资源调度中常见的帕累托最优分析框架，数值量级（80ms/150ms/200ms）在工程实践中合理，且内部逻辑自洽（低延迟需高命中率公有云，高延迟容忍度下自建固定成本优势显现）。

## Search Query

CDN P99 latency target strategy selection
