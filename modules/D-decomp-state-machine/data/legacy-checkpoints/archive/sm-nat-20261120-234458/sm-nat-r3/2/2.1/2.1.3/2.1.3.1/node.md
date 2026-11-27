# N110: 在容量受限场景下（假设缓存仅能容纳总对象数的50%，即K=50,000），LFU保留Top 50%热度对象，其字节命中率 H_LFU_50 = (Σ_{i=1}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

在容量受限场景下（假设缓存仅能容纳总对象数的50%，即K=50,000），LFU保留Top 50%热度对象，其字节命中率 H_LFU_50 = (Σ_{i=1}^{50000} q_i * s_i) / (Σ_{i=1}^{100000} q_i * s_i)，需基于Pareto(β=0.9)和Pareto(α=1.1)的联合分布计算分子分母。

## Corrected Claim

在容量受限场景下（假设缓存仅能容纳总对象数的50%，即K=50,000），LFU保留Top 50%热度对象，其字节命中率 H_LFU_50 = (Σ_{i=1}^{50000} q_i * s_i) / (Σ_{i=1}^{100000} q_i * s_i)，需基于Pareto(β=0.9)和Pareto(α=1.1)的联合分布计算分子分母。

## Evidence

先验知识/题面给定，逻辑校验通过
