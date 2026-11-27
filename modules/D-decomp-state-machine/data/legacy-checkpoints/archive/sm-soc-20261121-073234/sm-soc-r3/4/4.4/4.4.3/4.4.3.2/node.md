# N277: 干预后成交周期 T_with_intervention 的估计值可通过因果推断模型（如双重差分法或倾向得分匹配）在移除高价排序权重后的模拟环境中计算得出。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N91

## Claim

干预后成交周期 T_with_intervention 的估计值可通过因果推断模型（如双重差分法或倾向得分匹配）在移除高价排序权重后的模拟环境中计算得出。

## Corrected Claim

干预后成交周期 T_with_intervention 的估计值可通过因果推断模型（如双重差分法或倾向得分匹配）在模拟环境中计算得出，具体需结合业务场景定义干预变量（如移除高价排序权重）。

## Evidence

[质询]来源仅提及因果干预在推荐系统去偏中的应用，未直接支持‘移除高价排序权重’这一特定业务场景下的成交周期估计方法，存在场景不匹配风险。 | 来源[1]间接支持因果推断（如干预操作）可用于消除混淆因子影响，但未直接覆盖‘高价排序权重’与‘成交周期’的具体关联，属间接支持。

## Search Query

causal inference counterfactual time-to-sell after removing price ranking weight

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/499778810&rut=531341a06a62ab2ee33183bc0eda16b65aad6a3833ac2cc1f927c733bd576dc5', 'type': 'ddg', 'title': '因果中的干预（intervention）操作在机器学习中是如何实现的？'}
