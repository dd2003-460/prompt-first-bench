# N27: 平台搜索算法中，触发商品重新进入高频推荐流（重索引）的最小降价阈值 $\theta_{filter}$ 的具体数值为 5% 或 10%（即 $\Delta P 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

平台搜索算法中，触发商品重新进入高频推荐流（重索引）的最小降价阈值 $\theta_{filter}$ 的具体数值为 5% 或 10%（即 $\Delta P \ge 5\%$ 或 $10\%$），低于此阈值的降价操作在算法层面被视为噪声，不触发 $\Delta Q$ 的显著变化。

## Corrected Claim

平台搜索算法中，降价操作可能触发商品重新进入高频推荐流（重索引），但具体的最小降价阈值因平台、品类及算法版本而异，并非固定的5%或10%；低于一定阈值的微小价格变动通常被视为噪声，不显著影响排名。

## Evidence

[质询]该陈述声称存在一个具体的、通用的最小降价阈值（5%或10%）来触发重索引，这属于具体的工程参数或算法实现细节。然而，主流市场平台（如Facebook Marketplace、通用电商）的搜索和推荐算法通常是黑盒且动态调整的，并不存在公开文档证实存在这样一个固定的、跨平台通用的“5%或10%”硬性阈值。将复杂的动态排序因子简化为单一的固定百分比阈值，极可能是对算法机制的过度简化或错误归因。 | 参考来源[2]和[3]讨论了市场算法的排名、过滤和个性化机制，但均未提及具体的“5%或10%”降价阈值作为重索引的触发条件；来源[1]仅涉及二手市场搜索标签提取。由于缺乏直接来源支持这一具体数值，且该数值属于经验性工程参数而非第一性原理可推导事实，故降级为定性表述。

## Search Query

second hand marketplace search algorithm reindexing threshold price change percentage

## Retrieval Sources

- {'url': 'https://www.pixyle.ai/blog/improve-site-search-second-hand-marketplace-with-extracted-label-information&rut=4cef76f4bea616a3aeee3b056f3f9c4082c10969ad85b9c3993579774089788f', 'type': 'ddg', 'title': 'Enhancing Second-Hand Marketplace Search - pixyle.ai'}
- {'url': 'https://lucagency.net/blog/facebook-marketplace-algorithm-how-to-reset-your-feed-and-get-better-listings&rut=e7123de668ffcb155e224bb9e99766cecd6e8bf589c5d22369d05ef6b19a171f', 'type': 'ddg', 'title': 'Facebook Marketplace Algorithm: How to Reset Your Feed and Get Better ...'}
- {'url': 'https://vertexstack.io/blog/marketplace-search-matching-algorithms-ranking&rut=293d5a2b708544f4394733a59e6dd2b276327a4bbfd72def34b2db77c60b90c8', 'type': 'ddg', 'title': 'Marketplace search: ranking, filtering and personalization'}
