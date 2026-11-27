# N54: N16机制的边界失效条件：当商品具有强时效性（如季节性商品，剩余有效销售期 T_valid < 96h）或极高稀缺性（N_stock < 2）时，自动降价算法的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

N16机制的边界失效条件：当商品具有强时效性（如季节性商品，剩余有效销售期 T_valid < 96h）或极高稀缺性（N_stock < 2）时，自动降价算法的 2% 衰减率不足以覆盖时间价值，需引入修正系数 β = T_valid / T_standard，此时有效衰减率 α_eff = α * β。

## Corrected Claim

N16机制的边界失效条件：当商品具有强时效性（如季节性商品，剩余有效销售期 T_valid < 96h）或极高稀缺性（N_stock < 2）时，自动降价算法的 2% 衰减率不足以覆盖时间价值，需引入修正系数 β = T_valid / T_standard，此时有效衰减率 α_eff = α * β。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seasonal goods dynamic pricing algorithm correction factor scarcity stock level
