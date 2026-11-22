# N148: 历史数据回归估算 ΔP_entry 的具体方法：利用平台历史数据，构建逻辑回归模型 logit(P_entry) = β0 + β1*(P_floor/P_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

历史数据回归估算 ΔP_entry 的具体方法：利用平台历史数据，构建逻辑回归模型 logit(P_entry) = β0 + β1*(P_floor/P_market) + β2*Category_Dummy，通过 β1 的系数值量化价格下限变化对进入概率的边际影响，通常 β1 为负值且绝对值大于 1。

## Corrected Claim

历史数据回归估算 ΔP_entry 的具体方法：利用平台历史数据，构建逻辑回归模型 logit(P_entry) = β0 + β1*(P_floor/P_market) + β2*Category_Dummy，通过 β1 的系数值量化价格下限变化对进入概率的边际影响，通常 β1 为负值且绝对值大于 1。

## Evidence

先验知识/题面给定，逻辑校验通过：逻辑回归中系数符号与经济学直觉一致（价格下限相对市场价越高，进入概率越低，β1为负），且作为经验性回归模型，系数绝对值大于1在统计上完全合理，无内部矛盾。
