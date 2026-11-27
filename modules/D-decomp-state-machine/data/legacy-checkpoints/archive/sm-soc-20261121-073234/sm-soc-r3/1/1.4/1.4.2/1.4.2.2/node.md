# N142: 价格敏感度系数 k 在二手市场并非均匀分布，而是随商品稀缺性呈非单调变化：稀缺品 k 较低（买家对价格不敏感），普通品 k 较高；若统一取 k=1.0，会低估稀

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

价格敏感度系数 k 在二手市场并非均匀分布，而是随商品稀缺性呈非单调变化：稀缺品 k 较低（买家对价格不敏感），普通品 k 较高；若统一取 k=1.0，会低估稀缺品降价对CTR的衰减程度，导致模型偏差。

## Corrected Claim

价格敏感度系数 k 在二手市场并非均匀分布，而是随商品稀缺性呈非单调变化：稀缺品 k 较低（买家对价格不敏感），普通品 k 较高；若统一取 k=1.0，会低估稀缺品降价对CTR的衰减程度，导致模型偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：稀缺品通常具有更高的需求刚性（低价格敏感度），普通品竞争更激烈（高价格敏感度），该经济直觉符合市场规律，且统一参数确实会导致对稀缺品价格弹性估计偏差。

## Search Query

price elasticity of demand luxury vs commodity goods second hand market
