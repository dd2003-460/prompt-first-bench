# N209: KL散度计算的具体离散化公式：KL(P_obs || P_H0) = Σ p_i * ln(p_i / q_i)，其中p_i为观察到的15-25%区间内偏差分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

KL散度计算的具体离散化公式：KL(P_obs || P_H0) = Σ p_i * ln(p_i / q_i)，其中p_i为观察到的15-25%区间内偏差分布的直方图频率，q_i为H0正态分布在该区间的理论频率，需明确分箱宽度h以平衡偏差与方差。

## Corrected Claim

KL散度计算的具体离散化公式：KL(P_obs || P_H0) = Σ p_i * ln(p_i / q_i)，其中p_i为观察到的15-25%区间内偏差分布的直方图频率，q_i为H0正态分布在该区间的理论频率，需明确分箱宽度h以平衡偏差与方差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

KL divergence calculation discrete histogram pricing deviation
