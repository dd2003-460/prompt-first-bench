# N12: 工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_res 需缩短以维持命中率，但 C 固定，导致 H_static 下降。量化折扣因子 D = 1 - (1 - exp(-0.05*T_res))。

## Corrected Claim

工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_res 需缩短以维持命中率，但 C 固定，导致 H_static 下降。量化折扣因子 D = 1 - (1 - exp(-0.05*T_res))。

## Evidence

先验知识/题面给定，逻辑校验通过
