# N13: 买家效用函数：U_buyer = V_quality - P_price - C_search * T_deal，其中V_quality为质量价值（高质商品V=

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

买家效用函数：U_buyer = V_quality - P_price - C_search * T_deal，其中V_quality为质量价值（高质商品V=100，低质V=50），C_search为搜索成本（单位时间10），T_deal为成交周期（小时）。高挂价下买家预期V_quality=80，低挂价下预期V_quality=60。

## Corrected Claim

买家效用函数：U_buyer = V_quality - P_price - C_search * T_deal，其中V_quality为质量价值（高质商品V=100，低质V=50），C_search为搜索成本（单位时间10），T_deal为成交周期（小时）。高挂价下买家预期V_quality=80，低挂价下预期V_quality=60。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了效用函数中的'质量价值项'和'搜索成本项'，两者在概念上是正交的（不重复）。然而，父节点明确包含三个主要变量：V_quality, P_price, C_search/T_deal。子节点仅覆盖了 V_quality 和 C_search，完全遗漏了 'P_price'（价格项）的处理或定义，导致分解不完备。此外，子节点1中提到的'与题面给定的80存在偏差'属于数据校准问题，而非结构分解问题，但这不影响正交性判断，主要问题在于完备性缺失。）

## Search Query

buyer utility function quality value price search cost deal time
