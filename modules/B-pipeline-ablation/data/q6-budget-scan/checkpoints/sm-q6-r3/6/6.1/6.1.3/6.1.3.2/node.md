# N287: 公有云CDN API调用费用：假设日均管理操作及健康检查API调用10,000次，免费额度内无费用，超出部分单价0.01元/千次，若全部超出则月度API成本为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

公有云CDN API调用费用：假设日均管理操作及健康检查API调用10,000次，免费额度内无费用，超出部分单价0.01元/千次，若全部超出则月度API成本为 $C_{api} = (10000 \times 30 / 1000) \times 0.01 \text{ 元} = 3 \text{ 元/月}$，可忽略不计。

## Corrected Claim

公有云CDN API调用费用：假设日均管理操作及健康检查API调用10,000次，免费额度内无费用，超出部分单价0.01元/千次，若全部超出则月度API成本为 $C_{api} = (10000 \times 30 / 1000) \times 0.01 \text{ 元} = 3 \text{ 元/月}$，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (10000 * 30 / 1000) * 0.01 = 3 元/月 数学正确，量级合理，符合公有云API计费常见逻辑。

## Search Query

aliyun cdn api call pricing per 1000 calls
