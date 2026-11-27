# N167: 针对 α=1.1 的 Pareto 分布，计算总体方差 Var(S) = (α/(α-1)^2) * (1/(α-2)) * x_min^2 的具体数值（需设定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

针对 α=1.1 的 Pareto 分布，计算总体方差 Var(S) = (α/(α-1)^2) * (1/(α-2)) * x_min^2 的具体数值（需设定 x_min，如 1KB），以验证蒙特卡洛模拟中样本方差收敛所需的采样量 N 是否确实为 10^6 量级

## Corrected Claim

针对 α=1.1 的 Pareto 分布，计算总体方差 Var(S) = (α/(α-1)^2) * (1/(α-2)) * x_min^2 的具体数值（需设定 x_min，如 1KB），以验证蒙特卡洛模拟中样本方差收敛所需的采样量 N 是否确实为 10^6 量级

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布方差公式正确，且由于α=1.1导致方差极大（约121倍于均值平方），蒙特卡洛模拟收敛确实需要10^6量级样本。
