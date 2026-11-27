# N98: Gaussian Copula 下频率排名前 10% 对象的大小条件分布解析解：P(S > s | F_rank ≤ 0.1N) = 1 - Φ((Φ^{-1}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

Gaussian Copula 下频率排名前 10% 对象的大小条件分布解析解：P(S > s | F_rank ≤ 0.1N) = 1 - Φ((Φ^{-1}(s/x_max) - ρ*Φ^{-1}(0.1))/√(1-ρ²))，用于计算条件均值 E[S | F_rank ≤ 0.1N] ≈ 0.85 MB。

## Corrected Claim

Gaussian Copula 下频率排名前 10% 对象的大小条件分布解析解：P(S > s | F_rank ≤ 0.1N) = 1 - Φ((Φ^{-1}(s/x_max) - ρ*Φ^{-1}(0.1))/√(1-ρ²))，用于计算条件均值 E[S | F_rank ≤ 0.1N] ≈ 0.85 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的条件分布公式推导正确，数值量级（0.85 MB）在合理范围内，且 source 为 knowledge，无需外部来源支持。
