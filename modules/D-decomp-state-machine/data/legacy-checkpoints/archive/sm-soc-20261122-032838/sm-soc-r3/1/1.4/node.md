# N8: 降价无咨询机制：买家存在‘等待折扣’的行为惯性，其搜索过滤器隐含条件 $P_{current} < P_{min}$。当卖家从 $P_{high}$ 降至 $P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

降价无咨询机制：买家存在‘等待折扣’的行为惯性，其搜索过滤器隐含条件 $P_{current} < P_{min}$。当卖家从 $P_{high}$ 降至 $P_{low}$ 时，若 $P_{low}$ 仍高于买家心理阈值 $P_{threshold}$（由近期成交价 $P_{ref}$ 决定，$P_{threshold} \approx 0.9 P_{ref}$），则触发新咨询的概率 $P_{inquiry}$ 不随降价幅度线性增加，而是存在断点：若 $P_{low} > P_{threshold}$，则 $P_{inquiry} \approx 0$。

## Corrected Claim

降价无咨询机制：买家存在‘等待折扣’的行为惯性，其搜索过滤器隐含条件 $P_{current} < P_{min}$。当卖家从 $P_{high}$ 降至 $P_{low}$ 时，若 $P_{low}$ 仍高于买家心理阈值 $P_{threshold}$（由近期成交价 $P_{ref}$ 决定，$P_{threshold} \approx 0.9 P_{ref}$），则触发新咨询的概率 $P_{inquiry}$ 不随降价幅度线性增加，而是存在断点：若 $P_{low} > P_{threshold}$，则 $P_{inquiry} \approx 0$。

## Evidence

先验知识/题面给定，逻辑校验通过
