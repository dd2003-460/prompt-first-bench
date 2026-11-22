# N134: 上尾买家对价格不敏感的特征需要量化为价格弹性ε_tail，其数值显著低于市场平均弹性ε_avg，具体关系为 ε_tail = ε_avg * (1 - 0.7 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

上尾买家对价格不敏感的特征需要量化为价格弹性ε_tail，其数值显著低于市场平均弹性ε_avg，具体关系为 ε_tail = ε_avg * (1 - 0.7 * s_uniqueness)，其中s_uniqueness为商品独特性评分(0-1)。

## Corrected Claim

上尾买家对价格不敏感的特征通常表现为价格弹性 ε_tail 低于市场平均弹性 ε_avg，具体量化关系需根据商品独特性评分 s_uniqueness 通过实证数据拟合确定，而非固定公式。

## Evidence

[质询]该公式 ε_tail = ε_avg * (1 - 0.7 * s_uniqueness) 是一个具体的经验参数化模型，其中系数 0.7 和线性关系缺乏通用的经济学理论支持或广泛认可的实证标准，属于特定场景下的假设性建模，而非普适事实。 | 逻辑上自洽（独特性越高，弹性越低，符合直觉），但参考来源 [1][2][3] 仅讨论了价格弹性的定义、测量方法（PSM）和估算技术（Monodense），均未提及该特定公式或系数 0.7，属于经验事实且缺乏来源直接支持。

## Search Query

price elasticity tail buyers uniqueness score second-hand goods

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29048309/article/details/167553523&rut=09b998b6d5c248ffce146b2d04f2da5961629dfae0e19f58aed1ac8fbd473ce2', 'type': 'ddg', 'title': '弹性：量化价格与需求敏感度的核心分析工具 - Csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_71158509/article/details/136181027&rut=0267d4f52e91b0920a42d3279f9d74cbdb110601cd8655e0bde27ffc1d98d79b', 'type': 'ddg', 'title': '价格弹性分析：经济学工具在定价策略与市场决策中的应用-csdn博客'}
- {'url': 'https://hankli.space/blog-ai-enterprise-data/ai/2026/04/03/monodense-deep-neural-model-for-determin.html&rut=5b0d8a34052e13b1c0cd5e37ef6dc506aa5999ea56d1c68f35c3dff6305262ae', 'type': 'ddg', 'title': '用 Monodense 神经网络估算商品价格弹性：因果推断遇上单调性约束 | tHanks.log'}
