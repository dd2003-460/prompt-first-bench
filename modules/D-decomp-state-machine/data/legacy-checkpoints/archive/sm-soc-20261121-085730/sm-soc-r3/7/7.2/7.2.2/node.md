# N378: 上尾买家估值上限 V_max 的分布方差 σ_tail 与商品标准化程度负相关，具体关系为 σ_tail = σ_base * (1 - 0.5 * S_sta

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N133, N134, N135

## Claim

上尾买家估值上限 V_max 的分布方差 σ_tail 与商品标准化程度负相关，具体关系为 σ_tail = σ_base * (1 - 0.5 * S_standardization)，其中 S_standardization ∈ [0,1]，σ_base 需通过同类商品成交价的95th-99th百分位差值估算。

## Corrected Claim

上尾买家估值上限 V_max 的分布离散度通常与商品标准化程度负相关，但具体量化关系需基于特定市场数据回归得出，不宜直接采用固定线性公式。

## Evidence

[质询]该公式为特定模型假设，缺乏普适性理论支持；'95th-99th百分位差值'作为方差估算方法在统计上存在量纲和定义混淆（百分位差是范围而非标准差/方差），且系数0.5为任意设定，无实证或第一性原理依据。 | 经验事实/模型参数，逻辑校验发现统计定义混淆（用百分位差估算方差）且公式系数无依据，来源缺失无法验证。
