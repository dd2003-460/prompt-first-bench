# N362: C_algorithmic(D) 的衰减函数：假设推荐权重随价格偏离度呈指数衰减，C_algorithmic(D) = C_base * exp(-k_alg 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

C_algorithmic(D) 的衰减函数：假设推荐权重随价格偏离度呈指数衰减，C_algorithmic(D) = C_base * exp(-k_alg * D)，其中 k_alg 为算法惩罚系数，需通过日志分析确定（假设 k_alg=0.2/day 对应 15% 偏离时权重降至 0.74）。

## Corrected Claim

C_algorithmic(D) 的衰减函数假设推荐权重随价格偏离度呈指数衰减，形式为 C_base * exp(-k_alg * D)，其中 k_alg 为需通过日志分析确定的算法惩罚系数。

## Evidence

[质询]该陈述包含具体的经验参数（k_alg=0.2/day）和特定的衰减模型假设，属于经验事实而非第一性原理可推导的数学性质，且缺乏外部来源支持其具体数值或模型选择的合理性。 | 经验事实，逻辑自洽（数学计算 exp(-0.2*0.15)≈0.97 与文中 0.74 存在数值矛盾，但作为假设性参数设定，其内部逻辑结构自洽，仅因缺乏来源支持且数值示例可能有误而降级），缺来源支持。

## Search Query

recommendation system weight decay based on price deviation
