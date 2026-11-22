# N126: T_hot 的更新率主导公式修正：在全量驻留且无容量驱逐情况下，对象失效仅由更新引起，T_hot_eff = -ln(1 - P_inval_target) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

T_hot 的更新率主导公式修正：在全量驻留且无容量驱逐情况下，对象失效仅由更新引起，T_hot_eff = -ln(1 - P_inval_target) / u；若目标失效概率 P_inval=1%，则 T_hot_eff ≈ 0.01005 天 ≈ 14.5 分钟，而非原 claim 中的 1/u 量级。

## Corrected Claim

T_hot 的更新率主导公式修正：在全量驻留且无容量驱逐情况下，对象失效仅由更新引起，T_hot_eff = -ln(1 - P_inval_target) / u；若目标失效概率 P_inval=1%，则 T_hot_eff ≈ 0.01005 天 ≈ 14.5 分钟，而非原 claim 中的 1/u 量级。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型中，失效概率 P = 1 - e^(-uT)，解得 T = -ln(1-P)/u。当 P=0.01 时，-ln(0.99) ≈ 0.01005，量级与数值计算均正确。

## Search Query

cache invalidation rate update frequency mean time
