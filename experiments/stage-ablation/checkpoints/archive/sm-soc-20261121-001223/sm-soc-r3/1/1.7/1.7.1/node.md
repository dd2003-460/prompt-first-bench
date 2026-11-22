# N51: 买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C_search = T_search * r_time；需具体化 T_search 在二手平台的典型分布（如均值 30-60 分钟）及 r_time 的估算基准（如当地平均时薪的 10-20%）。

## Corrected Claim

买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C_search = T_search * r_time；需具体化 T_search 在二手平台的典型分布（如均值 30-60 分钟）及 r_time 的估算基准（如当地平均时薪的 10-20%）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式 C_search = T_search * r_time 中的两个独立变量。子节点1聚焦于 T_search 的分布特性与均值估算，子节点2聚焦于 r_time 的参数化与用户异质性。两者在定义域和逻辑维度上完全正交，且共同覆盖了父节点要求的具体化 T_search 分布和 r_time 估算基准，无内容遗漏或重复。）

## Search Query

second hand market search cost time opportunity cost estimation
