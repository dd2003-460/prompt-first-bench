# N35: P99延迟约束下的最大允许传播延迟：若目标 P99 ≤ 100ms，且处理+排队延迟平均为 20ms，则允许的最大传播延迟 t_prop_max = 100 -

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

P99延迟约束下的最大允许传播延迟：若目标 P99 ≤ 100ms，且处理+排队延迟平均为 20ms，则允许的最大传播延迟 t_prop_max = 100 - 20 = 80ms；对应最大物理距离 d_max_prop = 80ms * 150km/ms = 12,000km（单程），但考虑到往返RTT，实际单程距离上限约为 6,000km。

## Corrected Claim

P99延迟约束下的最大允许传播延迟：若目标 P99 ≤ 100ms，且处理+排队延迟平均为 20ms，则允许的最大传播延迟 t_prop_max = 100 - 20 = 80ms；对应最大物理距离 d_max_prop = 80ms * 150km/ms = 12,000km（单程），但考虑到往返RTT，实际单程距离上限约为 6,000km。

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300km/ms，光纤中约150km/ms，80ms单程对应12000km，往返RTT对应单程6000km，计算自洽。
