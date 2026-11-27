# N12: 工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_res 需缩短以维持命中率，但 C 固定，导致 H_static 下降。量化折扣因子 D = 1 - (1 - exp(-0.05*T_res))。

## Corrected Claim

工作点 1（高频更新，λ=0.05/day）：极端失效场景。有效命中率 H_eff = H_static * (1 - P_invalid)。当 λ 升高，T_res 需缩短以维持命中率，但 C 固定，导致 H_static 下降。量化折扣因子 D = 1 - (1 - exp(-0.05*T_res))。

## Evidence

父节点级核验未通过：不完备（父节点明确定义了有效命中率 H_eff 及其与折扣因子 D 的关联，并指出 T_res 缩短导致 H_static 下降的机制。子节点仅量化了 H_static_high 的下降，完全遗漏了父节点中关于折扣因子 D 的计算以及 H_eff 最终如何结合 H_static 和 P_invalid 进行推导的关键步骤。）
