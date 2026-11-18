# N139: 工作点 C 对象（热度排名 10%-100%）的字节流量占比 ByteShare_C 的计算式：ByteShare_C = Σ_{i=10^4}^{10^5} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

工作点 C 对象（热度排名 10%-100%）的字节流量占比 ByteShare_C 的计算式：ByteShare_C = Σ_{i=10^4}^{10^5} (λ_i * s_i) / Σ_{i=1}^{10^5} (λ_i * s_i)，其中分子和分母均需基于 Pareto 分布参数进行数值计算。

## Corrected Claim

工作点 C 对象（热度排名 10%-100%）的字节流量占比 ByteShare_C 的计算式：ByteShare_C = Σ_{i=10^4}^{10^5} (λ_i * s_i) / Σ_{i=1}^{10^5} (λ_i * s_i)，其中分子和分母均需基于 Pareto 分布参数进行数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
