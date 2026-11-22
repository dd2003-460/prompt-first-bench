# N292: Holt-Winters 模型中，季节性波动对 Δt_avg 置信区间宽度的具体贡献量化：CI_width_Q4 = CI_width_base * (1 + 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

Holt-Winters 模型中，季节性波动对 Δt_avg 置信区间宽度的具体贡献量化：CI_width_Q4 = CI_width_base * (1 + λ_season * |Seasonal_Index_Q4 - 1|)，其中 λ_season 为季节敏感度系数（需通过历史数据回归确定，假设 λ_season=0.5），Seasonal_Index_Q4 为 Q4 季节指数（通常 > 1），该公式直接解释为何 CI 从 [10%, 20%] 扩展至 [7.5%, 22.5%]。

## Corrected Claim

在特定假设下，若采用启发式公式 CI_width_Q4 = CI_width_base * (1 + λ_season * |Seasonal_Index_Q4 - 1|) 且 λ_season=0.5，可解释置信区间宽度的扩展，但该公式非 Holt-Winters 标准统计推导，需结合具体历史数据回归验证其有效性。

## Evidence

[质询]该公式为人为构造的启发式模型，并非 Holt-Winters 模型的标准统计推导结果；Holt-Winters 的置信区间通常基于残差方差和预测误差分布计算，而非通过简单的线性乘法因子（1 + λ * |S-1|）直接缩放基础区间宽度。此外，从 [10%, 20%] 扩展到 [7.5%, 22.5%] 意味着区间中心从 15% 移动到了 15%（(7.5+22.5)/2=15），但宽度从 10% 增加到了 15%，这暗示了不对称扩展或中心点未变但半径增大，而公式给出的乘数因子通常作用于半宽，若基础半宽为 5%，乘以 (1+0.5*|S-1|) 得到新半宽，需验证具体数值是否吻合，且该公式缺乏统计学上的严谨推导支持。 | 先验知识/题面给定，逻辑校验通过（公式在数学上可自洽解释区间变化，但作为通用统计结论缺乏理论依据，属于特定假设下的工程近似）

## Search Query

Holt-Winters seasonal index confidence interval width expansion Q4 e-commerce
