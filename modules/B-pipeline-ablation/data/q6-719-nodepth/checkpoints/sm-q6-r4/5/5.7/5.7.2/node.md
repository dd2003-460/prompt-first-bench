# N158: 单POP月度机房租赁及电力成本 C_pop_maintenance = P_rack * N_racks + P_power * PUE * N_racks *

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

单POP月度机房租赁及电力成本 C_pop_maintenance = P_rack * N_racks + P_power * PUE * N_racks * 24h * 30d，其中 P_rack (机柜月租) 约为 3000-8000 元/机柜，N_racks 约为 1-2 个/POP，P_power (单柜功耗) 约为 5-8 kW，PUE 通常为 1.3-1.5

## Corrected Claim

单POP月度机房租赁及电力成本 C_pop_maintenance = P_rack * N_racks + P_power * PUE * N_racks * 24h * 30d，其中 P_rack (机柜月租) 约为 3000-8000 元/机柜，N_racks 约为 1-2 个/POP，P_power (单柜功耗) 约为 5-8 kW，PUE 通常为 1.3-1.5

## Evidence

父节点级核验未通过：有冗余（子节点分别代表高成本（一线/高功耗）和低成本（二三线/低功耗）两种典型场景，逻辑上互斥且无矛盾（正交性满足）。两者共同覆盖了父节点参数范围内的主要分布情况（完备性满足）。然而，这两个子节点本质上是同一个公式在不同参数取值下的计算结果，属于参数化的变体而非独立的概念分解，因此存在结构性冗余。）
