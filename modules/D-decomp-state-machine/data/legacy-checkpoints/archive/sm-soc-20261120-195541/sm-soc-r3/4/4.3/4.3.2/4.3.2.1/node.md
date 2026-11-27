# N144: Q_intentional 的计算分母 N_total_queries 应限定为'降价后48小时内针对该特定商品ID或同类目关键词的搜索请求总数'，分子 N_i

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

Q_intentional 的计算分母 N_total_queries 应限定为'降价后48小时内针对该特定商品ID或同类目关键词的搜索请求总数'，分子 N_intentional 为其中包含商品核心属性词（如品牌、型号、关键特征）的查询数，以排除泛搜索噪声。

## Corrected Claim

Q_intentional 的计算分母 N_total_queries 应限定为'降价后48小时内针对该特定商品ID或同类目关键词的搜索请求总数'，分子 N_intentional 为其中包含商品核心属性词（如品牌、型号、关键特征）的查询数，以排除泛搜索噪声。

## Evidence

先验知识/题面给定，逻辑校验通过
