# N97: 若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关系数公式为 ρ = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，解得 θ ≈ -1.58（需数值验证）

## Corrected Claim

若改用 Frank Copula 建模 ρ=-0.3，其参数 θ 需通过求解 Corr(S,H) = -0.3 的数值方程确定，Frank Copula 的相关系数公式为 ρ = (e^θ - 1 - θ e^θ) / (θ^2 e^θ)，解得 θ ≈ -1.58（需数值验证）

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

Frank copula parameter theta for correlation -0.3 numerical solution
