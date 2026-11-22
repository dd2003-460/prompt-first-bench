# N51: H100 SXM 单卡/双卡/四卡配置下，基于 1.3 倍冗余系数，电源瓦数下限分别为 910W/1820W/3640W，对应电源效率（80+ Titanium

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

H100 SXM 单卡/双卡/四卡配置下，基于 1.3 倍冗余系数，电源瓦数下限分别为 910W/1820W/3640W，对应电源效率（80+ Titanium）对实际功耗的影响分别为 5%/4%/3%。

## Corrected Claim

H100 SXM 单卡/双卡/四卡配置下，基于 1.3 倍冗余系数，电源瓦数下限分别为 910W/1820W/3640W，对应电源效率（80+ Titanium）对实际功耗的影响分别为 5%/4%/3%。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在严重数值矛盾（单卡/双卡/四卡计算结果与父节点声明的910W/1820W/3640W完全不符），且前三个子节点结构高度重复，本质上是同一公式在不同GPU数量下的参数化实例，应合并。）

## Search Query

NVIDIA H100 SXM multi-GPU PSU efficiency 80+ Titanium power loss
