# N183: 成交周期显著性检验的方差估计：计算成交周期 T_deal 的标准差 σ_T。假设 T_deal 服从对数正态分布，σ_T = T_old * sqrt(σ_ln

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N60

## Claim

成交周期显著性检验的方差估计：计算成交周期 T_deal 的标准差 σ_T。假设 T_deal 服从对数正态分布，σ_T = T_old * sqrt(σ_ln²)，其中 σ_ln 为对数周期的标准差。需确定 σ_ln 的经验值（如 0.5），以计算检验 ΔT/T < -0.10 的 p 值。

## Corrected Claim

成交周期显著性检验的方差估计：若假设成交周期 T_deal 服从对数正态分布，其标准差 σ_T 可通过对数周期的标准差 σ_ln 估算（σ_T ≈ T_old * sqrt(e^{σ_ln²} - 1) 或近似为 T_old * σ_ln 当 σ_ln 较小时）。需根据具体市场数据确定 σ_ln 的经验值以计算 p 值。

## Evidence

[质询]该陈述包含具体的经验参数（σ_ln = 0.5）和特定的统计假设（对数正态分布），属于经验事实范畴，无法从第一性原理严格推出，且参考来源未提供该特定场景下的方差估计方法或经验值支持。 | 逻辑上，若T服从对数正态分布，其标准差确实与对数标准差相关，公式推导自洽；但来源[1]仅讨论一般t检验，未覆盖对数正态分布假设或具体经验值，属于经验事实缺来源支持。

## Search Query

log-normal distribution selling time standard deviation e-commerce

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/94429164&rut=108dffd92ae10335e62a413aac121d91a5213fcc4f3007bfe7fbee70a1b70370', 'type': 'ddg', 'title': '假设检验（t分布），参数估计与置信区间Alevel Further Statistics'}
