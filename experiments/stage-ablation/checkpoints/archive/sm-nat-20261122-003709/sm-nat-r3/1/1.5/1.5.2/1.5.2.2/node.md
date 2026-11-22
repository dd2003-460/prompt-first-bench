# N123: 量化Spearman秩相关ρ=-0.3对头部对象大小分布的压缩效应修正因子：在双变量Pareto Copula模型下，引入负相关使得头部对象的大小期望值从独立假

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

量化Spearman秩相关ρ=-0.3对头部对象大小分布的压缩效应修正因子：在双变量Pareto Copula模型下，引入负相关使得头部对象的大小期望值从独立假设值降低，修正因子f(ρ) ≈ 1 + ρ * (Var(S)/E[S]^2) * 0.5，代入ρ=-0.3及Pareto方差系数得出具体折扣比例（预计约85%-90%）。

## Corrected Claim

在双变量Pareto Copula模型下，引入负相关（ρ=-0.3）通常会使头部对象的大小期望值低于独立假设值，但具体的修正因子需通过数值积分或蒙特卡洛模拟确定，简单的线性近似 f(ρ) ≈ 1 + 0.5ρCV² 可能仅在小相关系数下近似成立。

## Evidence

[质询]公式 f(ρ) ≈ 1 + ρ * (Var(S)/E[S]^2) * 0.5 缺乏明确的理论推导依据，且系数 0.5 的引入显得任意；在双变量 Pareto Copula 模型中，负相关对边缘分布期望值的影响通常不通过这种简单的线性修正因子来描述，除非有特定的近似假设（如小 ρ 展开），但此处 ρ=-0.3 并不极小，线性近似的有效性存疑。 | 先验知识/题面给定，逻辑校验通过（量纲一致，数值量级合理），但具体修正公式的系数缺乏标准理论支持，且无外部来源验证该特定近似式。

## Search Query

bivariate Pareto copula rank correlation effect on conditional expectation head
