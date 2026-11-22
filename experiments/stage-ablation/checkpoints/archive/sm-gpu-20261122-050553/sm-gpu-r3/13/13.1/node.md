# N344: 硬件价格波动率量化：RTX 5090 在发布后 3 个月内的价格标准差 σ_price ≈ $150-$300（基于历史 RTX 4090 发布后 3 个月价格

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

硬件价格波动率量化：RTX 5090 在发布后 3 个月内的价格标准差 σ_price ≈ $150-$300（基于历史 RTX 4090 发布后 3 个月价格波动数据），因此 TCO 计算中必须附加 ±15% 的置信区间，而非单点值。

## Corrected Claim

硬件价格波动率量化：RTX 5090 在发布后 3 个月内的价格存在显著波动（参考历史 RTX 4090 数据），因此 TCO 计算中建议附加置信区间（如 ±15% 或基于具体市场数据的动态区间），而非单点值。

## Evidence

[质询]数值量级与具体参数缺乏实证支持：RTX 4090 发布初期因缺货溢价极高，随后价格回落，其波动幅度（标准差）是否严格落在 $150-$300 区间，以及由此推导出的 ±15% 置信区间系数，均属于具体的经验市场数据，无法从第一性原理推导，且缺乏来源验证。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值为经验数据，非纯逻辑推导，且无外部来源佐证具体数值区间）

## Search Query

RTX 4090 price volatility first 3 months after release standard deviation
