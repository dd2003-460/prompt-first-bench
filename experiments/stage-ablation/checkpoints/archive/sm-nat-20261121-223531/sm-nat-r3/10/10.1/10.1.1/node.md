# N227: D = 1 - E[P_stale | Byte Weighted] 的积分展开：D = 1 - [∫ (1 - e^{-0.01 * 1/h}) * s(h)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

D = 1 - E[P_stale | Byte Weighted] 的积分展开：D = 1 - [∫ (1 - e^{-0.01 * 1/h}) * s(h) * f_{S,H}(s,h) dsdh] / E[S]，其中 E[S] = ∫ s * f_{S,H}(s,h) dsdh，需将联合分布 f_{S,H} 参数化。

## Corrected Claim

D = 1 - E[P_stale | Byte Weighted] 的积分展开：D = 1 - [∫ (1 - e^{-0.01 * 1/h}) * s(h) * f_{S,H}(s,h) dsdh] / E[S]，其中 E[S] = ∫ s * f_{S,H}(s,h) dsdh，需将联合分布 f_{S,H} 参数化。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于全概率公式和期望定义，将离散求和推广为连续积分，量纲与逻辑自洽。
