# N100: A100 80GB SXM4 版本因无NVLink桥接（需PCIe或专用底板）导致多卡互联成本增加，单卡现货价约为 $9,000-$11,000，其PCIe版本

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

A100 80GB SXM4 版本因无NVLink桥接（需PCIe或专用底板）导致多卡互联成本增加，单卡现货价约为 $9,000-$11,000，其PCIe版本（A100 PCIe 80GB）价格略低约 $500-$800，但带宽降低，影响多卡方案吞吐 [时效待核]

## Corrected Claim

A100 80GB SXM4 版本因需专用底板及NVLink桥接，多卡互联硬件成本高于PCIe版本；其单卡市场价格通常高于A100 PCIe 80GB版本，但PCIe版本因带宽限制会影响多卡方案吞吐。具体价格随市场波动，需实时查询。

## Evidence

[质询]该陈述包含具体的市场价格区间（$9,000-$11,000）和差价（$500-$800），属于典型的市场经验事实，且标注了[时效待核]。由于缺乏实时市场数据支持，具体数值极易随时间波动而失效，且不同渠道（现货/期货/不同地区）价格差异巨大，单一静态数值区间缺乏普适性。 | 逻辑上，SXM4版本因需要专用底板（Baseboard）和NVLink桥接，硬件复杂度和成本确实高于PCIe版本，且PCIe版本带宽较低，符合硬件工程常识。但作为source=search节点，具体价格属于经验事实，且本轮检索无可用来源支持，无法验证具体数值，故降级。

## Search Query

A100 80GB SXM vs PCIe price difference 2024
