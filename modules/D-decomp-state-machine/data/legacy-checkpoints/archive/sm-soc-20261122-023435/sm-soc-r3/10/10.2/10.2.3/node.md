# N254: w_T 权重随 P 变化的函数形式：w_T(P) = w_T_max * sigmoid((P - P_min) / σ_P)，其中 w_T_max 为最大权重

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

w_T 权重随 P 变化的函数形式：w_T(P) = w_T_max * sigmoid((P - P_min) / σ_P)，其中 w_T_max 为最大权重，σ_P 为过渡带宽（如 10 元）；当 P < P_min 时，w_T 显著下降，趋近于 0。

## Corrected Claim

w_T 权重随 P 变化的函数形式可能采用 Sigmoid 函数，如 w_T(P) = w_T_max * sigmoid((P - P_min) / σ_P)，其中 w_T_max 为最大权重，σ_P 为过渡带宽；当 P < P_min 时，w_T 显著下降，趋近于 0。

## Evidence

[质询]该陈述描述了一个具体的经验性数学模型（Sigmoid函数形式及参数定义），属于经验事实/模型假设范畴，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持其作为通用标准或特定系统的确切定义。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

dynamic weight adjustment in recommendation algorithms based on price
