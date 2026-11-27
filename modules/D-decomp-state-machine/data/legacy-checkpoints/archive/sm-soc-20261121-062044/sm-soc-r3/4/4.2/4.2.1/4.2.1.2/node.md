# N199: 中性价比最优工作点：引入基准点依赖修正项，定义 λ_corrected = λ_base * (1 + α_ref * |P_ref - P_market| /

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

中性价比最优工作点：引入基准点依赖修正项，定义 λ_corrected = λ_base * (1 + α_ref * |P_ref - P_market| / P_market)，其中 P_ref 为卖家心理基准价，α_ref 为基准敏感度系数（通常 0.1-0.3）；若 P_ref = P_markup_max，则 λ_corrected ≈ 1.25 * 1.2 = 1.5，仍低于 2.25，提示需加入概率权重扭曲项 w(p) = p^γ / (p^γ + (1-p)^γ)^{1/γ}。

## Corrected Claim

中性价比最优工作点：引入基准点依赖修正项，定义 λ_corrected = λ_base * (1 + α_ref * |P_ref - P_market| / P_market)，其中 P_ref 为卖家心理基准价，α_ref 为基准敏感度系数；若 P_ref = P_markup_max，则 λ_corrected 可能显著高于基准值，提示需考虑加入概率权重扭曲项 w(p) 以调整风险偏好。

## Evidence

[质询]该陈述包含具体的经验参数（α_ref 范围 0.1-0.3）和特定的数学模型推导（λ_corrected 数值及 w(p) 公式），属于经验事实/模型设定，无法从第一性原理严格推出，且缺乏外部来源支持其具体数值和公式的普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

prospect theory reference point dependence loss aversion calibration probability weighting gamma
