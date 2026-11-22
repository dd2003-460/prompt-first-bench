# N291: Impressions_target 的最优解：Impressions_target = argmin C_traffic s.t. ΔQ_comp >= ΔQ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

Impressions_target 的最优解：Impressions_target = argmin C_traffic s.t. ΔQ_comp >= ΔQ_required，其中 ΔQ_required 为维持咨询率不降所需的最低咨询量提升；通过拉格朗日乘子法求解，最优 Impressions_target 与 ΔQ_required 呈线性关系，斜率由 η_comp 决定。

## Corrected Claim

Impressions_target 的最优解：Impressions_target = argmin C_traffic s.t. ΔQ_comp >= ΔQ_required，其中 ΔQ_required 为维持咨询率不降所需的最低咨询量提升；通过拉格朗日乘子法求解，最优 Impressions_target 与 ΔQ_required 呈线性关系，斜率由 η_comp 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：在标准线性规划或二次规划优化模型中，若目标函数和约束条件均为线性（或凸二次），拉格朗日对偶理论表明最优解与约束右端项（此处为ΔQ_required）通常呈线性关系，斜率由边际成本/效率参数（η_comp）决定，符合经济学直觉。

## Search Query

optimal impression target for inquiry rate maintenance
