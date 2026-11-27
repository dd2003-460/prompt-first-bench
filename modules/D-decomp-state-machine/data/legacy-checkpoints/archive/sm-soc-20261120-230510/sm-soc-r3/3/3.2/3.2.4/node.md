# N62: 转化率 Conversion_Rate 的量化构成：Conversion_Rate = f(CTR, Purchase_Intent, P_ask)，其中 CT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

转化率 Conversion_Rate 的量化构成：Conversion_Rate = f(CTR, Purchase_Intent, P_ask)，其中 CTR 为点击率，Purchase_Intent 为购买意向，P_ask 为挂价；Purchase_Intent 与 P_ask 负相关。

## Corrected Claim

转化率 Conversion_Rate 的量化构成：Conversion_Rate = f(CTR, Purchase_Intent, P_ask)，其中 CTR 为点击率，Purchase_Intent 为购买意向，P_ask 为挂价；Purchase_Intent 与 P_ask 负相关。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了购买意向（Purchase_Intent）的微观构成，子节点2将其代入父节点公式并引入挂价（P_ask）作为自变量，明确了转化率随价格变化的函数关系及敏感度分解方法。两者分别关注“结构定义”与“价格敏感性/动态关系”，无逻辑冲突或内容重叠，且共同覆盖了父节点中所有变量（CTR, Purchase_Intent, P_ask）及其相互关系。）
