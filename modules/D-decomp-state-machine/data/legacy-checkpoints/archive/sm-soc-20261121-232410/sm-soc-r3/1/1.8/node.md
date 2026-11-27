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

父节点级核验未通过：不完备（子节点1关注质量价值的期望计算（V_quality项），子节点2关注搜索成本的时间分解（C_search与T_deal项），两者分别处理效用函数中不同的变量成分，因此正交且不冗余。然而，父节点中明确包含价格项 P_price，且效用函数为 U = V - P - C*T。现有的两个子节点仅覆盖了 V_quality 和 C_search/T_deal，完全遗漏了 P_price（价格）对效用的影响及其可能的不确定性或谈判机制，导致分解不完备。）

## Search Query

buyer utility function quality value price search cost deal time
