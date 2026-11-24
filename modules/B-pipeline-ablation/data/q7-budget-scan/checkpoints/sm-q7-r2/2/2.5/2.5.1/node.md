# N75: HDD单盘功耗参数：企业级HDD（如Seagate Exos X18、WD Ultrastar DC HC550）典型功耗为8-15W/盘，单盘容量18TB-2

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

HDD单盘功耗参数：企业级HDD（如Seagate Exos X18、WD Ultrastar DC HC550）典型功耗为8-15W/盘，单盘容量18TB-22TB，平均功耗密度约为0.4-0.8W/TB（以18TB盘为例，10W/18TB≈0.56W/TB），修正N16中2W/TB为0.5-1W/TB区间

## Corrected Claim

企业级HDD（如Seagate Exos X18）单盘容量为18TB，典型功耗密度约为0.5-1W/TB（基于行业典型功耗8-15W估算）。

## Evidence

[质询]参考来源仅提及希捷Exos X18的容量和兼容性，未提供具体的功耗数值（如8-15W）或功耗密度计算，无法直接验证具体参数值。 | 逻辑推导成立（10W/18TB≈0.56W/TB），但参考来源[1]仅确认了18TB容量，未提供功耗数据，属于经验事实且缺乏直接来源支持。

## Search Query

enterprise HDD power consumption watts per drive Seagate Exos X18 WD Ultrastar DC HC550 datasheet

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/273629008&rut=22eb2d88c0be85ff7918bc0f5c9c0b8c500296e7546299be46b5171fbb5eb706', 'type': 'ddg', 'title': '有容乃大，18T企业级机械硬盘旗舰—希捷银河Exos X18测试'}
