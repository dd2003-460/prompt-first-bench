# N141: 核密度估计（KDE）参数选择对拐点识别的影响：带宽 h 的选择遵循 Silverman 规则 h = 1.06 * σ * n^(-1/5)，需说明不同带宽下 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

核密度估计（KDE）参数选择对拐点识别的影响：带宽 h 的选择遵循 Silverman 规则 h = 1.06 * σ * n^(-1/5)，需说明不同带宽下 Skew(P_ask) 阈值从 0.5 偏移至 0.4-0.6 的范围，以及拐点位置 P* 的误差棒。

## Corrected Claim

核密度估计（KDE）参数选择对拐点识别的影响：带宽 h 的选择遵循 Silverman 规则 h = 1.06 * σ * n^(-1/5)，需说明不同带宽下 Skew(P_ask) 阈值从 0.5 偏移至 0.4-0.6 的范围，以及拐点位置 P* 的误差棒。

## Evidence

先验知识/题面给定，逻辑校验通过：Silverman规则公式正确，KDE带宽敏感性导致统计量（如偏度）及拐点位置存在合理波动范围，符合统计学原理。
