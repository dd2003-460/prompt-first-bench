# N156: C_search^prior 的量化分解：C_search^prior = T_search_prior * W_time + C_cognitive_prio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

C_search^prior 的量化分解：C_search^prior = T_search_prior * W_time + C_cognitive_prior。其中 T_search_prior 为无信号时的平均搜索时间（假设 30 分钟），W_time 为时间价值（假设 $0.5/分钟），C_cognitive_prior 为认知负荷成本（假设 $2）。则 C_search^prior = 30*0.5 + 2 = $17。

## Corrected Claim

C_search^prior 的量化分解：C_search^prior = T_search_prior * W_time + C_cognitive_prior。其中 T_search_prior 为无信号时的平均搜索时间（假设 30 分钟），W_time 为时间价值（假设 $0.5/分钟），C_cognitive_prior 为认知负荷成本（假设 $2）。则 C_search^prior = 30*0.5 + 2 = $17。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本分解逻辑，数值计算 30*0.5 + 2 = 17 准确无误，假设参数在合理量级范围内。

## Search Query

search cost decomposition time value cognitive load
