# N30: Gaussian Copula 联合分布构造：定义 S' = Φ_S(S) 和 F' = Φ_F(F) 为边缘分布的 CDF 变换，联合 CDF 为 C(u,v

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Gaussian Copula 联合分布构造：定义 S' = Φ_S(S) 和 F' = Φ_F(F) 为边缘分布的 CDF 变换，联合 CDF 为 C(u,v; ρ) = Φ_2(u,v; ρ)，其中 ρ=-0.3，用于生成符合负相关约束的 (S_i, F_i) 样本对。

## Corrected Claim

Gaussian Copula 联合分布构造：定义 S' = Φ_S(S) 和 F' = Φ_F(F) 为边缘分布的 CDF 变换，联合 CDF 为 C(u,v; ρ) = Φ_2(u,v; ρ)，其中 ρ=-0.3，用于生成符合负相关约束的 (S_i, F_i) 样本对。

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 构造联合分布的标准方法即为对边缘变量应用 CDF 变换后通过二元正态 CDF 耦合，ρ=-0.3 符合负相关约束，数学定义自洽。
