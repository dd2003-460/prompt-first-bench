# N103: K_noise 的统计特性：扣除周期性与事件性成分后，剩余流量噪声服从零均值高斯分布，标准差 σ_noise ≈ 5%-10% 的当前基线流量；该噪声导致缓存命

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N25

## Claim

K_noise 的统计特性：扣除周期性与事件性成分后，剩余流量噪声服从零均值高斯分布，标准差 σ_noise ≈ 5%-10% 的当前基线流量；该噪声导致缓存命中率 H(t) 在稳态值附近 ±2%-5% 波动，进而影响回源率 R_back(t) 的尾部风险。

## Corrected Claim

K_noise 的统计特性：扣除周期性与事件性成分后，剩余流量噪声服从零均值高斯分布，标准差 σ_noise ≈ 5%-10% 的当前基线流量；该噪声导致缓存命中率 H(t) 在稳态值附近 ±2%-5% 波动，进而影响回源率 R_back(t) 的尾部风险。

## Evidence

先验知识/题面给定，逻辑校验通过
