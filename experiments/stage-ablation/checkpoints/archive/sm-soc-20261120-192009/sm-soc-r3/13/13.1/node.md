# N352: 算法权重比值 w_ctr/w_conversion 的逆向工程估计：利用平台公开 API 或爬虫数据，构建回归模型 ln(Rank_Score) = β_ctr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

算法权重比值 w_ctr/w_conversion 的逆向工程估计：利用平台公开 API 或爬虫数据，构建回归模型 ln(Rank_Score) = β_ctr * ln(CTR) + β_conv * ln(Conversion_Rate) + ε，计算比值 R = β_ctr / β_conv；若 R > 2.0 且 p < 0.05，则证实平台算法更重视点击率而非成交率。

## Corrected Claim

一种可能的逆向工程估计方法是：利用平台公开数据构建回归模型 ln(Rank_Score) = β_ctr * ln(CTR) + β_conv * ln(Conversion_Rate) + ε，通过计算比值 R = β_ctr / β_conv 来评估平台对点击率与成交率的相对重视程度，但具体阈值（如 R > 2.0）和统计显著性标准需根据具体数据分布和假设检验结果确定，而非固定为 p < 0.05 即证实。

## Evidence

[质询]该陈述描述了一种具体的逆向工程方法论（回归模型构建及阈值判定），属于经验性操作指南而非第一性原理可推导的数学事实。此外，参考来源仅涉及CTR预估的Baseline代码，未包含任何关于通过回归分析反推平台算法权重比值（w_ctr/w_conversion）的具体方法、阈值（R>2.0）或统计显著性标准（p<0.05）的支持证据，存在来源不相关且缺乏直接支持的问题。 | 逻辑上，利用对数线性回归估计权重比值在计量经济学和算法分析中是合理的方法，量纲和逻辑自洽；但参考来源[1]仅展示CTR预估模型，与该逆向工程方法无关，无法提供外部支持，且该事实属于经验性方法论，非第一性原理可推导，故降级。

## Search Query

eBay algorithm ranking factors CTR vs conversion rate weight

## Retrieval Sources

- {'url': 'https://github.com/creatorwyx/TAAC2026-CTR-Baseline&rut=5df20cb6bbcd18bf6fe062ebef2e0a2cbe33dc16c298524c490626ee8ba84d07', 'type': 'ddg', 'title': 'GitHub - creatorwyx/TAAC2026-CTR-Baseline: 2026腾讯广告算法大赛 CTR 预估 Baseline ...'}
