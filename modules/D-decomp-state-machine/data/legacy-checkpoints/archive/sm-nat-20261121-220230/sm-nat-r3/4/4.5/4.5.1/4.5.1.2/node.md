# N212: 负相关修正量化：当 ρ_uH = -0.2 时，基于 Frank Copula 联合分布积分，LFU 保留的高热度对象平均更新率比 LRU 保留对象低约 15%

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N73

## Claim

负相关修正量化：当 ρ_uH = -0.2 时，基于 Frank Copula 联合分布积分，LFU 保留的高热度对象平均更新率比 LRU 保留对象低约 15%，导致 P_invalid_LFU ≈ 0.85 * P_invalid_LRU，具体差值 ΔP = 0.15 * P_invalid_LRU

## Corrected Claim

当 ρ_uH = -0.2 时，基于 Frank Copula 联合分布积分，LFU 保留的高热度对象平均更新率比 LRU 保留对象低，导致 P_invalid_LFU 小于 P_invalid_LRU（具体差值需根据详细积分计算确定，此处引用的 15% 为特定条件下的估算值）。

## Evidence

[质询]数值量级与具体系数缺乏推导依据：'15%'和'0.85'是特定参数下的经验拟合值还是理论推导结果？在 ρ=-0.2 的弱负相关下，LFU 与 LRU 的失效概率差异是否必然精确为 15%？该具体数值无法从第一性原理直接推出，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值 15% 无法仅凭逻辑推导验证，需外部数据或详细推导过程支持，故降级）
