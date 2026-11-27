# N31: Pareto(β=0.9) 热度分布的累积分布函数 (CDF) 参数化：F(q) = 1 - (q_min/q)^(1-β) 对于 q >= q_min，其中 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Pareto(β=0.9) 热度分布的累积分布函数 (CDF) 参数化：F(q) = 1 - (q_min/q)^(1-β) 对于 q >= q_min，其中 q_min=1 次/天，β=0.9；该分布意味着 P(q > 100) = (1/100)^0.1 ≈ 0.63，表明 63% 的对象访问频率低于 100 次/天，头部集中度极高。

## Corrected Claim

Pareto(β=0.9) 热度分布的累积分布函数 (CDF) 参数化：F(q) = 1 - (q_min/q)^(1-β) 对于 q >= q_min，其中 q_min=1 次/天，β=0.9；该分布意味着 P(q > 100) = (1/100)^0.1 ≈ 0.63，表明 63% 的对象访问频率低于 100 次/天，头部集中度极高。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式正确，代入q=100, q_min=1, β=0.9计算得P(q>100)=(1/100)^(1-0.9)=100^-0.1≈0.63，数值量级与逻辑自洽。

## Search Query

Pareto distribution CDF parameter beta 0.9
