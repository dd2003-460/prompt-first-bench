# N237: 共享随机源对卖家收益的乘性影响项量化为 Var(ΔR_seller | ε_market) = (∂R_seller/∂D)² * σ²_market，其中 ∂

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N72

## Claim

共享随机源对卖家收益的乘性影响项量化为 Var(ΔR_seller | ε_market) = (∂R_seller/∂D)² * σ²_market，其中 ∂R_seller/∂D 为卖家收益对需求量的弹性系数；当 ε_market 为正（需求上行）时，高挂价卖家的成交概率 p_match 增加，导致 ΔR_seller 的方差结构呈现右偏特征。

## Corrected Claim

共享随机源对卖家收益的影响可近似量化为 Var(ΔR_seller | ε_market) ≈ (∂R_seller/∂D)² * σ²_market，其中 ∂R_seller/∂D 为卖家收益对需求量的边际敏感度；当 ε_market 为正时，高挂价卖家的成交概率 p_match 增加，导致 ΔR_seller 的分布呈现右偏特征。

## Evidence

[质询]公式量纲与定义混淆：将收益对需求的导数 (∂R/∂D) 称为'弹性系数'在术语上不准确（弹性通常指相对变化率），且该公式隐含了收益对需求呈线性响应且无其他噪声源的强假设，忽略了匹配概率 p_match 的非线性饱和效应及市场微观结构噪声，导致方差估计可能严重偏离实际。 | 先验知识/题面给定，逻辑校验通过（公式结构符合一阶泰勒展开近似，但术语'弹性系数'使用不严谨且忽略了非线性匹配机制，故降级为定性表述）

## Search Query

stochastic demand shock impact on seller revenue variance elasticity
