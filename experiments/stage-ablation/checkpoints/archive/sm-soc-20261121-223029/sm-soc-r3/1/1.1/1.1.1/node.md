# N35: P_ref（同类商品近期成交均价）的具体定义窗口为过去7天或30天，且需指定为成交中位数而非算术平均值，以消除极端值对基准价的扰动。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

P_ref（同类商品近期成交均价）的具体定义窗口为过去7天或30天，且需指定为成交中位数而非算术平均值，以消除极端值对基准价的扰动。

## Corrected Claim

P_ref（同类商品近期成交均价）通常基于过去7天或30天的成交数据计算，且常采用成交中位数而非算术平均值，以消除极端值对基准价的扰动。

## Evidence

父节点级核验未通过：有冗余（子节点A和B本质上是同一参数（时间窗口 T_window）的两个不同取值，属于冗余分解。虽然它们在灵敏度/稳定性上形成对比，但在逻辑结构上应合并为‘时间窗口选择策略’，而非两个独立的正交维度。统计量选择（子节点C）是独立且必要的，与时间窗口正交。）

## Search Query

second hand marketplace price reference window median vs mean
