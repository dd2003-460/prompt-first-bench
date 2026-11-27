# N215: 独立假设下缓存前10%最热门对象所需的总字节数 B_indep 的解析表达式：B_indep = N * 0.1 * E[S]，其中 N=100,000，E[S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

独立假设下缓存前10%最热门对象所需的总字节数 B_indep 的解析表达式：B_indep = N * 0.1 * E[S]，其中 N=100,000，E[S] 为截断 Pareto(α=1.1, S_max) 的期望大小。

## Corrected Claim

独立假设下缓存前10%最热门对象所需的总字节数 B_indep 的解析表达式：B_indep = N * 0.1 * E[S]，其中 N=100,000，E[S] 为截断 Pareto(α=1.1, S_max) 的期望大小。

## Evidence

先验知识/题面给定，逻辑校验通过：在独立假设下，每个对象被缓存的概率为0.1，总字节数为对象数乘以单个对象期望大小，公式推导正确。
