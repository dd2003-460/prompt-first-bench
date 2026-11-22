# N27: 买家单次搜索的时间成本 $C_{time}$ 量化为：$C_{time} = w_{time} \times t_{search}$，其中 $w_{time}$

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

买家单次搜索的时间成本 $C_{time}$ 量化为：$C_{time} = w_{time} \times t_{search}$，其中 $w_{time}$ 为买家时间机会成本（元/小时），$t_{search}$ 为平均单次比价耗时（分钟/次），二手平台典型值需结合用户画像调研确定。

## Corrected Claim

买家单次搜索的时间成本可初步建模为 $C_{time} = w_{time} \times t_{search}$，其中 $w_{time}$ 为买家时间机会成本（元/小时），$t_{search}$ 为平均单次比价耗时（分钟/次）；该线性模型为简化假设，实际应用中需结合用户画像调研及行为数据校准，并考虑非线性因素。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数区间下的两个特例（冗余），且仅覆盖了两个极端工作点，未覆盖中间连续区间或一般性推导逻辑（不完备）。）

## Search Query

second hand marketplace buyer time cost of comparison shopping average time per search
