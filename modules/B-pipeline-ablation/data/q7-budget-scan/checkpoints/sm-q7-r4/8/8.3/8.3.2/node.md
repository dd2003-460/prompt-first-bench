# N271: 散热风扇功耗非线性修正：P_fan 并非简单的 0.1 * P_total，而是与总热量的 0.75 次方成正比（遵循流体动力学定律），且在低温环境（<20°C

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

散热风扇功耗非线性修正：P_fan 并非简单的 0.1 * P_total，而是与总热量的 0.75 次方成正比（遵循流体动力学定律），且在低温环境（<20°C）下风扇转速可大幅降低，实际 P_fan 通常为 20-40W（针对 1kW 级别 IT 负载），而非 100W+

## Corrected Claim

散热风扇功耗非线性修正：P_fan 并非简单的 0.1 * P_total，而是与总热量的 0.75 次方成正比（遵循流体动力学定律），且在低温环境（<20°C）下风扇转速可大幅降低，实际 P_fan 通常为 20-40W（针对 1kW 级别 IT 负载），而非 100W+

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一物理模型在不同负载水平下的数值实例化（参数取值），而非概念上的正交维度；此外，父节点明确提到的‘低温环境（<20°C）’这一关键边界条件在三个子节点中均未体现，导致完备性缺失。）

## Search Query

server cooling fan power consumption non-linear relationship heat dissipation
