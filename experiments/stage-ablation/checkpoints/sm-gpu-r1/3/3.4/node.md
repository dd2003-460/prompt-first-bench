# N17: 多卡TCO修正项：多卡方案需增加PCIe/NVLink带宽成本、散热成本（风扇/机柜）及故障率（MTBF降低）。2x消费卡的TCO = 2*Hardware_C

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

多卡TCO修正项：多卡方案需增加PCIe/NVLink带宽成本、散热成本（风扇/机柜）及故障率（MTBF降低）。2x消费卡的TCO = 2*Hardware_Cost + 1.2*Power_Cost (散热效率降低) + 0.1*Hardware_Cost (故障冗余预留)。若单卡数据卡（如A6000）性能/价格比高于2x消费卡10%以上，则单卡方案在TCO上更优。

## Corrected Claim

多卡TCO修正项：多卡方案需增加PCIe/NVLink带宽成本、散热成本（风扇/机柜）及故障率（MTBF降低）。2x消费卡的TCO = 2*Hardware_Cost + 1.2*Power_Cost (散热效率降低) + 0.1*Hardware_Cost (故障冗余预留)。若单卡数据卡（如A6000）性能/价格比高于2x消费卡10%以上，则单卡方案在TCO上更优。

## Evidence

先验知识/题面给定，逻辑校验通过
