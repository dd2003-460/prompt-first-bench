# N238: 共享随机源对买家福利的乘性影响项量化为 Var(ΔC_buyer | ε_market) = (∂C_buyer/∂D)² * σ²_market，其中 ∂C_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N72

## Claim

共享随机源对买家福利的乘性影响项量化为 Var(ΔC_buyer | ε_market) = (∂C_buyer/∂D)² * σ²_market，其中 ∂C_buyer/∂D 为买家搜索成本对需求密度的敏感系数；在需求高峰期（ε_market > 0），商品密度增加导致搜索效率提升，ΔC_buyer 的方差减小，表现为负相关效应。

## Corrected Claim

共享随机源对买家福利的乘性影响项量化为 Var(ΔC_buyer | ε_market) = (∂C_buyer/∂D)² * σ²_market，其中 ∂C_buyer/∂D 为买家搜索成本对需求密度的敏感系数；在需求高峰期（ε_market > 0），商品密度增加导致搜索效率提升，ΔC_buyer 的方差减小，表现为负相关效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述基于条件方差公式 Var(X|Y) = E[Var(X|Y)] + Var(E[X|Y]) 的简化应用，在局部线性近似下，若市场冲击 ε_market 通过需求密度 D 影响成本 C，且 D 与 C 呈负相关（密度高效率高），则条件方差确实与敏感系数的平方及市场方差成正比，逻辑自洽。

## Search Query

buyer search cost variance impact of market demand density shock
