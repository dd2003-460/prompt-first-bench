# N261: 回源带宽修正因子 η 对有效命中率的影响为 H_effective = H_base * η + (1 - η) * H_degraded，其中 H_degra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

回源带宽修正因子 η 对有效命中率的影响为 H_effective = H_base * η + (1 - η) * H_degraded，其中 H_degraded 为带宽不足时的降级命中率（通常比 H_base 低5-10%）

## Corrected Claim

回源带宽修正因子 η 对有效命中率的影响为 H_effective = H_base * η + (1 - η) * H_degraded，其中 H_degraded 为带宽不足时的降级命中率（通常比 H_base 低5-10%）

## Evidence

先验知识/题面给定，逻辑校验通过
