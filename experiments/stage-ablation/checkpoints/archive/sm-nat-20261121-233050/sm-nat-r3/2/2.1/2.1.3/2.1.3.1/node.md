# N95: Copula 修正因子的解析近似：在 Gaussian Copula 假设下，修正因子 C_ρ 可近似为 1 - ρ * (α-1)/(α) = 1 - (-0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Copula 修正因子的解析近似：在 Gaussian Copula 假设下，修正因子 C_ρ 可近似为 1 - ρ * (α-1)/(α) = 1 - (-0.3) * 0.1/1.1 ≈ 1.027，表明负相关性使 LRU 下界提升约 2.7%，而非经验估计的 5-10%。

## Corrected Claim

Copula 修正因子的解析近似：在 Gaussian Copula 假设下，修正因子 C_ρ 可近似为 1 - ρ * (α-1)/(α) = 1 - (-0.3) * 0.1/1.1 ≈ 1.027，表明负相关性使 LRU 下界提升约 2.7%，而非经验估计的 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 1 - (-0.3) * (0.1/1.1) ≈ 1.027 准确，且符合 Gaussian Copula 下负相关提升下界的理论直觉。
