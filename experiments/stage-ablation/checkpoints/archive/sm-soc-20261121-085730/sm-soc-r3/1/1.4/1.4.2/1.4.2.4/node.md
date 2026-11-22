# N173: 商品标准化程度 S_std 的量化定义：S_std = 1 - (Var(P) / Mean(P)^2)，即变异系数的倒数归一化，S_std ∈ [0, 1]，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54, N55, N56

## Claim

商品标准化程度 S_std 的量化定义：S_std = 1 - (Var(P) / Mean(P)^2)，即变异系数的倒数归一化，S_std ∈ [0, 1]，其中 Var(P) 为同类商品成交价方差，Mean(P) 为均价，需通过平台历史成交数据的统计量计算。

## Corrected Claim

商品标准化程度 S_std 的一种量化定义为 S_std = 1 - (Var(P) / Mean(P)^2)，其中 Var(P) 为同类商品成交价方差，Mean(P) 为均价。注意：该值仅在变异系数 CV <= 1 时落在 [0, 1] 区间内，否则需进行截断处理或重新定义。

## Evidence

[质询]该定义属于特定模型或论文中的自定义指标，并非通用的统计学或经济学标准定义；且数学上 S_std 仅在 Var(P) >= 0 且 Mean(P) > 0 时有意义，若 Var(P) > Mean(P)^2（即变异系数 CV > 1），则 S_std 为负值，超出 [0, 1] 区间，陈述中声称 S_std ∈ [0, 1] 存在逻辑漏洞（除非隐含截断或特定数据分布假设）。 | 无可用外部来源支持该特定公式定义；逻辑校验发现公式在 CV>1 时会导致结果超出声称的 [0,1] 范围，存在内部逻辑不严谨之处。

## Search Query

product standardization index coefficient of variation price variance marketplace
