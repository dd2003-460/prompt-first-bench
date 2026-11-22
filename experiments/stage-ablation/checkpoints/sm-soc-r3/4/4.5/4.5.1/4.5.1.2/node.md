# N234: σ_wtp 的异质性来源分解：σ_wtp = sqrt(σ_budget² + σ_perception²)，其中 σ_budget 为买家预算分布标准差，σ_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

σ_wtp 的异质性来源分解：σ_wtp = sqrt(σ_budget² + σ_perception²)，其中 σ_budget 为买家预算分布标准差，σ_perception 为质量感知不确定性标准差；在长尾品类中 σ_perception 占比超过 60%，导致整体 σ_wtp 显著高于标品。

## Corrected Claim

σ_wtp 的异质性通常可分解为预算分布标准差（σ_budget）和质量感知不确定性标准差（σ_perception）的贡献；在长尾品类中，由于信息不对称，σ_perception 往往是主要驱动因素，导致整体 σ_wtp 高于标品。

## Evidence

[质询]该分解公式假设预算差异与感知不确定性相互独立且方差可加，但在实际市场中，高预算买家往往对质量感知更敏锐（或反之），两者可能存在相关性（协方差项），导致简单平方和公式在逻辑上过于简化；此外，'长尾品类中σ_perception占比超过60%'是一个具体的经验统计结论，缺乏普遍适用的理论推导支持。 | 先验知识/题面给定，逻辑校验通过（方差分解框架在独立假设下成立，量级合理），但具体占比数值为经验事实，无来源支持，故降级。

## Search Query

willingness to pay variance heterogeneity budget perception uncertainty
