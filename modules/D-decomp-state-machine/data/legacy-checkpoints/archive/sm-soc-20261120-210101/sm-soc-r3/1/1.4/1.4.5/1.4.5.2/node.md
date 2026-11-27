# N181: β_q 的估计方法：通过非线性最小二乘法拟合历史成交数据 (P_i, Q_i) 到 Q(P) = Q_0 * exp(-β_q * (P - P_clear)^

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

β_q 的估计方法：通过非线性最小二乘法拟合历史成交数据 (P_i, Q_i) 到 Q(P) = Q_0 * exp(-β_q * (P - P_clear)^2 / P_clear)。假设拟合得到的 β_q = 2.0，意味着价格偏离清算价 10% 时，成交量下降至 exp(-0.02) ≈ 98%。

## Corrected Claim

β_q 的估计方法：通过非线性最小二乘法拟合历史成交数据 (P_i, Q_i) 到 Q(P) = Q_0 * exp(-β_q * (P - P_clear)^2 / P_clear)。若拟合得到的 β_q = 2.0，则意味着价格偏离清算价 10% 时，成交量下降至 exp(-0.02) ≈ 98%。

## Evidence

[质询]该陈述包含具体的经验参数（β_q = 2.0）及基于此参数的具体数值推演，属于经验事实而非纯数学推导；且检索无可用来源，无法验证该特定参数值在真实市场数据中的有效性或普遍性。 | 经验事实，逻辑自洽但缺来源支持。数学计算正确：exp(-2.0 * 0.1^2) = exp(-0.02) ≈ 0.9802，即98%。但β_q=2.0为假设值，无外部数据佐证。

## Search Query

quadratic price sensitivity coefficient estimation demand function
