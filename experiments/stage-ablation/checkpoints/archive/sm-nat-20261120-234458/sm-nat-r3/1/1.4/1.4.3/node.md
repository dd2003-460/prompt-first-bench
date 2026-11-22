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

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且互不重叠：节点1处理归一化常数（因β<1导致积分发散需截断），节点2确定截断上界q_max（基于业务约束），节点3利用前两步结果计算修正后的概率并指出父节点错误。三者分别解决定义域、参数确定和最终推导，无重复或矛盾，且共同覆盖了修正父节点错误所需的所有数学步骤。）

## Search Query

Pareto distribution CDF parameter beta 0.9
