# N180: 风险调整后效用函数 U(ΔProfit) 的参数化：U(ΔProfit) = E[ΔProfit] - 0.5 * λ_risk * Var(ΔProfit)，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

风险调整后效用函数 U(ΔProfit) 的参数化：U(ΔProfit) = E[ΔProfit] - 0.5 * λ_risk * Var(ΔProfit)，其中 λ_risk 为卖家风险厌恶系数，需通过卖家历史定价行为或问卷量化 λ_risk 的分布。

## Corrected Claim

风险调整后效用函数 U(ΔProfit) 常采用均值-方差形式近似，如 U(ΔProfit) ≈ E[ΔProfit] - 0.5 * λ_risk * Var(ΔProfit)，其中 λ_risk 为风险厌恶系数，其具体数值需根据卖家偏好通过实证数据或问卷估计。

## Evidence

[质询]该陈述将风险调整后效用函数具体参数化为均值-方差形式（Mean-Variance Utility），并指定了特定的系数（0.5）和量化方法（历史行为/问卷）。虽然均值-方差效用是经济学中常见的近似，但并非唯一的或绝对正确的效用函数形式（例如，其他风险度量如CVaR或不同的效用函数形状可能更适用），且具体的系数0.5和量化方法属于经验性建模选择，缺乏普适的理论必然性。 | 逻辑自洽，均值-方差效用函数是标准的经济学建模工具，但具体参数化形式和量化方法属于经验事实/建模假设，且无外部来源支持，故降级。

## Search Query

seller risk aversion coefficient pricing behavior second-hand market
