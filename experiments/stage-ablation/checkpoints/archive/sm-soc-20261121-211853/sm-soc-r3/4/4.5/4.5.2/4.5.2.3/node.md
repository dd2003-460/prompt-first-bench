# N110: 流量波动标准差 $\sigma$ 的异质性修正：不同品类（如电子产品 vs 服装）的流量波动率存在显著差异。定义品类调整因子 $\sigma_{cat} = \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

流量波动标准差 $\sigma$ 的异质性修正：不同品类（如电子产品 vs 服装）的流量波动率存在显著差异。定义品类调整因子 $\sigma_{cat} = \sigma_{base} \times \kappa_{cat}$，其中 $\kappa_{cat}$ 为品类波动系数。高流动性品类（如手机）$\kappa_{cat} \approx 0.8$，低流动性品类（如古董）$\kappa_{cat} \approx 1.5$。MDE 计算必须使用品类特定的 $\sigma_{cat}$，否则会导致阈值偏差。

## Corrected Claim

流量波动标准差 $\sigma$ 的异质性修正：不同品类（如电子产品 vs 服装）的流量波动率存在显著差异。定义品类调整因子 $\sigma_{cat} = \sigma_{base} \times \kappa_{cat}$，其中 $\kappa_{cat}$ 为品类波动系数。高流动性品类（如手机）$\kappa_{cat} \approx 0.8$，低流动性品类（如古董）$\kappa_{cat} \approx 1.5$。MDE 计算必须使用品类特定的 $\sigma_{cat}$，否则会导致阈值偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
