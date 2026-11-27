# N38: 算法权重修正项：实际推荐权重 W_rec = (1 + α * ΔP) * (1 - β * T_stock) + ε_traffic，其中T_stock为商品

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

算法权重修正项：实际推荐权重 W_rec = (1 + α * ΔP) * (1 - β * T_stock) + ε_traffic，其中T_stock为商品上架时长，β为时间衰减系数，用于防止长期未成交的高价商品持续占用流量，需验证β是否足以抵消α带来的高挂价优势。

## Corrected Claim

在特定推荐算法设计中，可能采用形如 W_rec = (1 + α * ΔP) * (1 - β * T_stock) + ε_traffic 的权重修正项，其中β用于时间衰减，但需通过具体参数调优和A/B测试验证其有效性，而非默认成立。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在逻辑重叠（均围绕β是否足以抵消α的影响）且未覆盖父节点中ε_traffic（流量噪声/探索项）对权重修正的影响，导致不完备；同时两个子节点本质上都在验证β的阈值，属于冗余分解。）

## Search Query

recommendation weight time decay coefficient beta stock age high price bias correction
