# N43: 分母 Σ_{i=1}^{N} r_i · s_i 的解析近似：总字节请求量 = R_total * E[S]，其中 R_total=50M/day，E[S] 为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分母 Σ_{i=1}^{N} r_i · s_i 的解析近似：总字节请求量 = R_total * E[S]，其中 R_total=50M/day，E[S] 为对象大小的无条件期望（由 N30 给出）；该值代表工作负载的总字节流量，作为命中率的分母基准。

## Corrected Claim

分母 Σ_{i=1}^{N} r_i · s_i 的解析近似：总字节请求量 = R_total * E[S]，其中 R_total=50M/day，E[S] 为对象大小的无条件期望（由 N30 给出）；该值代表工作负载的总字节流量，作为命中率的分母基准。

## Evidence

先验知识/题面给定，逻辑校验通过：总字节流量定义为请求数乘以平均对象大小，符合基本定义。
