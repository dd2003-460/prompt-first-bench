# N88: LFU 实际命中率 H_LFU 的衰减修正：H_LFU = R_byte_TopK * (1 - Staleness_Penalty_LFU)；Stalenes

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

LFU 实际命中率 H_LFU 的衰减修正：H_LFU = R_byte_TopK * (1 - Staleness_Penalty_LFU)；Staleness_Penalty_LFU 由对象更新率 λ=0.01/day 和 LFU 策略下头部对象的平均驻留时间 T_res_LFU 决定，需计算 T_res_LFU 以量化因内容更新导致的失效损失。

## Corrected Claim

LFU 实际命中率 H_LFU 的衰减修正：H_LFU = R_byte_TopK * (1 - Staleness_Penalty_LFU)；Staleness_Penalty_LFU 由对象更新率 λ=0.01/day 和 LFU 策略下头部对象的平均驻留时间 T_res_LFU 决定，需计算 T_res_LFU 以量化因内容更新导致的失效损失。

## Evidence

先验知识/题面给定，逻辑校验通过
