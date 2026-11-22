# N186: 新鲜度权重 w_recency 的具体数值：通常设为 0.4 以激励新商品上架，但需验证其是否导致高挂价新商品获得额外曝光加成（Score_Recency * 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

新鲜度权重 w_recency 的具体数值：通常设为 0.4 以激励新商品上架，但需验证其是否导致高挂价新商品获得额外曝光加成（Score_Recency * w_recency > 阈值）。

## Corrected Claim

新鲜度权重 w_recency 的具体数值需根据业务场景通过实验确定，不存在通用的'通常值'（如 0.4）；需验证其是否导致高挂价新商品获得额外曝光加成，具体验证逻辑取决于系统评分公式的设计。

## Evidence

[质询]数值量级与具体参数缺乏依据：'通常设为 0.4' 是一个具体的经验参数，不同业务场景（如电商、新闻、社交）中新鲜度权重的设定差异巨大，且通常需要通过 A/B 测试或离线评估确定，不存在通用的'通常值'。此外，'Score_Recency * w_recency > 阈值' 这一具体验证逻辑也是特定系统的设计细节，并非通用标准。 | 经验事实，逻辑自洽但缺来源支持。参考来源 [1] 和 [2] 仅讨论了新鲜度加权的一般概念或 RAG 中的时间先验，未提供具体的权重数值（如 0.4）或特定的曝光加成验证公式；来源 [3] 涉及 RFM 分析，与推荐系统新鲜度权重无直接关联。

## Search Query

e-commerce platform algorithm ranking weight recency impact on new listings

## Retrieval Sources

- {'url': 'https://www.saber.app/glossary/recency-weighted-score&rut=753b898c2e889a9d478faaabde81483f34d463c637949a3f1f3047643922a8fc', 'type': 'ddg', 'title': 'Recency-Weighted Score: Definition, Examples & Use Cases'}
- {'url': 'https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.175832475.57637876/v1&rut=90943b863e8e57f517aaf48051048c779e812c9f4ae2529932b562682eec5fea', 'type': 'ddg', 'title': 'Solving Freshness in RAG: A Simple Recency Prior and the Limits of ...'}
- {'url': 'https://blog.csdn.net/weixin_44481878/article/details/90180452&rut=94aa3b9a0310ba9da1327115c571d5d309a3b629895b9612b28ff61faf52a80f', 'type': 'ddg', 'title': 'RFM分析（Recency，Frequency，Monetary） - CSDN博客'}
