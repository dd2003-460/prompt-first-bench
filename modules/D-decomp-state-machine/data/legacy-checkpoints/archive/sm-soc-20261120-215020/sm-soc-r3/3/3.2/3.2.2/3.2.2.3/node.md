# N132: 点击率下降 $CTR_{drop}$ 的分解：$CTR_{drop} = \Delta CTR_{price} + \Delta CTR_{trust} + \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

点击率下降 $CTR_{drop}$ 的分解：$CTR_{drop} = \Delta CTR_{price} + \Delta CTR_{trust} + \Delta CTR_{visibility}$；其中 $\Delta CTR_{price}$ 为正向（因价格更低），$\Delta CTR_{trust}$ 为负向，$\Delta CTR_{visibility}$ 为因曝光位置变化导致的被动变化；需通过控制曝光位置不变的实验数据，分离出纯信任效应 $\Delta CTR_{trust}$ 的具体数值范围。

## Corrected Claim

点击率下降 $CTR_{drop}$ 的分解：$CTR_{drop} = \Delta CTR_{price} + \Delta CTR_{trust} + \Delta CTR_{visibility}$；其中 $\Delta CTR_{price}$ 为正向（因价格更低），$\Delta CTR_{trust}$ 为负向，$\Delta CTR_{visibility}$ 为因曝光位置变化导致的被动变化；需通过控制曝光位置不变的实验数据，分离出纯信任效应 $\Delta CTR_{trust}$ 的具体数值范围。

## Evidence

先验知识/题面给定，逻辑校验通过：CTR分解为价格、信任和可见性效应符合因果推断基本逻辑，且明确指出了通过控制变量实验分离信任效应的必要性，无内部矛盾。
