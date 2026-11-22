# N206: 方差分解正交性验证：检验 Var(Price) ≈ Var(Signal) + Var(Noise) 是否成立，计算残差项 R = Var(Price) - V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

方差分解正交性验证：检验 Var(Price) ≈ Var(Signal) + Var(Noise) 是否成立，计算残差项 R = Var(Price) - Var(Signal) - Var(Noise)，若 |R| / Var(Price) < 0.05，则分解有效；若 R > 0.05 * Var(Price)，则存在未捕获的协方差项 Cov(Signal, Noise)，需检查 P_avg 计算窗口是否引入自相关或测量误差。

## Corrected Claim

方差分解正交性验证：检验 Var(Price) ≈ Var(Signal) + Var(Noise) 是否成立，计算残差项 R = Var(Price) - Var(Signal) - Var(Noise)，若 |R| / Var(Price) < 0.05，则分解有效；若 R > 0.05 * Var(Price)，则存在未捕获的协方差项 Cov(Signal, Noise)，需检查 P_avg 计算窗口是否引入自相关或测量误差。

## Evidence

先验知识/题面给定，逻辑校验通过
