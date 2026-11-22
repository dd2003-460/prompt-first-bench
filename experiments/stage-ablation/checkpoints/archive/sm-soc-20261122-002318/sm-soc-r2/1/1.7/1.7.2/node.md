# N51: 匹配率 M_rate 的具体计算依赖于买家保留价分布的右偏特性：当挂价溢价 Premium ∈ [15%, 25%] 时，M_rate 等于保留价分布 F(R)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

匹配率 M_rate 的具体计算依赖于买家保留价分布的右偏特性：当挂价溢价 Premium ∈ [15%, 25%] 时，M_rate 等于保留价分布 F(R) 的尾部概率 P(R ≥ P_market * (1 + Premium))，需结合 N8 中的 σ_noise 计算该分位数。

## Corrected Claim

匹配率 M_rate 的具体计算依赖于买家保留价分布的右偏特性：当挂价溢价 Premium ∈ [15%, 25%] 时，M_rate 等于保留价分布 F(R) 的尾部概率 P(R ≥ P_market * (1 + Premium))，需结合 N8 中的 σ_noise 计算该分位数。

## Evidence

先验知识/题面给定，逻辑校验通过：匹配率定义为保留价低于市场价的概率，即 P(R < P_market*(1+Premium))，其补集为尾部概率 P(R ≥ P_market*(1+Premium))，逻辑自洽且量纲正确。
