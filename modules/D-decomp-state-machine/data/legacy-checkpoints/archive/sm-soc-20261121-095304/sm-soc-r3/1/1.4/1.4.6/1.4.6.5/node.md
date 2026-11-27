# N119: C_handling（物流/包装边际成本）在同城面交场景下近似为 0 元，而在跨省快递场景下，对于重量 < 1kg 的普通商品，C_handling 基准值为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N40, N41

## Claim

C_handling（物流/包装边际成本）在同城面交场景下近似为 0 元，而在跨省快递场景下，对于重量 < 1kg 的普通商品，C_handling 基准值为 12 元（含包装耗材），重量每增加 1kg 增加 5 元。

## Corrected Claim

C_handling（物流/包装边际成本）在同城面交场景下近似为 0 元，而在跨省快递场景下，对于重量 < 1kg 的普通商品，C_handling 基准值为 12 元（含包装耗材），重量每增加 1kg 增加 5 元。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cross-province express delivery cost 12 yuan packaging cost 5 yuan per kg
