# N312: 蒙特卡洛收敛性判据的量化验证：设定N=1000次采样，计算TCO分布的标准差σ_N；再设N=5000次采样，计算σ_5000；若|σ_1000 - σ_5000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

蒙特卡洛收敛性判据的量化验证：设定N=1000次采样，计算TCO分布的标准差σ_N；再设N=5000次采样，计算σ_5000；若|σ_1000 - σ_5000| / σ_5000 < 1%，则视为收敛；否则需增加N至10,000或改用解析法（基于各变量方差合成：Var(TCO) = Var(P) + Var(E) + Var(M)）

## Corrected Claim

蒙特卡洛收敛性判据的量化验证：设定N=1000次采样，计算TCO分布的标准差σ_N；再设N=5000次采样，计算σ_5000；若|σ_1000 - σ_5000| / σ_5000 < 1%，则视为收敛；否则需增加N至10,000或改用解析法（基于各变量方差合成：Var(TCO) = Var(P) + Var(E) + Var(M)）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Monte Carlo convergence criterion standard deviation difference 1%
