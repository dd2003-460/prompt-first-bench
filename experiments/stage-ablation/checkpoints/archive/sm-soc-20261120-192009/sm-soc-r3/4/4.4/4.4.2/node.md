# N87: 稀缺度混杂控制变量：引入同类商品库存量 I_t 或在售数量 N_seller，回归模型 Y = β0 + β1*Price_High + β4*I_t + ε，

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

稀缺度混杂控制变量：引入同类商品库存量 I_t 或在售数量 N_seller，回归模型 Y = β0 + β1*Price_High + β4*I_t + ε，若 β1 显著则稀缺度非混杂。

## Corrected Claim

稀缺度混杂控制变量：引入同类商品库存量 I_t 或在售数量 N_seller，回归模型 Y = β0 + β1*Price_High + β4*I_t + ε，若 β1 显著则稀缺度非混杂。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于变量I_t的定义及多重共线性诊断（VIF/r），子节点2聚焦于回归系数β4的方向性检验及检验力问题，两者在统计检验的维度上（共线性 vs 显著性/检验力）是正交的，没有重复或矛盾。然而，父节点明确提到了两个可选的混杂控制变量：I_t（库存量）和 N_seller（在售数量）。子节点仅详细展开了 I_t 的处理逻辑，完全缺失了关于 N_seller 的定义、共线性检查及效应检验的内容，导致未覆盖父节点的所有关键方面。）
