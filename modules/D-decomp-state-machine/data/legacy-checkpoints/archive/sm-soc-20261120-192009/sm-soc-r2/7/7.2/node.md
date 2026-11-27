# N105: 曝光权重函数参数：平台算法中点击率权重 α 与成交速度权重 β 的具体数值或比例关系；需检索特定平台（如闲鱼、eBay）的公开技术文档或逆向工程研究。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

曝光权重函数参数：平台算法中点击率权重 α 与成交速度权重 β 的具体数值或比例关系；需检索特定平台（如闲鱼、eBay）的公开技术文档或逆向工程研究。

## Corrected Claim

平台算法中点击率与成交速度等指标通常作为排序因子，但具体权重参数（α, β）多为商业机密，缺乏公开的确切数值或固定比例关系，需依赖非公开的逆向工程或内部文档获取。

## Evidence

[质询]该陈述声称存在具体的数值或比例关系，但主流电商平台（如闲鱼、eBay）的排序算法属于核心商业机密，通常不会公开具体的权重参数（α, β）的精确数值。此外，参考来源仅涉及推荐系统的一般性评价指标定义，并未提供特定平台的逆向工程数据或具体参数值，因此无法证实存在公开的“具体数值”。 | 参考来源[1][2]仅介绍推荐系统通用指标，未包含特定平台（闲鱼/eBay）的算法参数细节，属于间接相关但无直接支持；鉴于具体参数为经验事实且缺乏公开来源支持，判定为degraded。

## Search Query

eBay Xianyu recommendation algorithm weighting click through rate transaction speed parameters

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2295919&rut=3ec8cbc5c8bf9236c2e3c5383db5a4336c359229f0977f48bd28666ab0b2f421', 'type': 'ddg', 'title': '深度学习应用篇-推荐系统 [11]：推荐系统的组成、场景转化指标（pv点击率,uv点击率,曝光点击率）、用户数据指标等评价指标详解'}
- {'url': 'https://cloud.tencent.com/developer/article/2338219&rut=d066ae6d71d41b2cb4c3f3e4cd5f2335fab6e3dcea5b6618f739cb7d826e26b7', 'type': 'ddg', 'title': '深度学习应用篇-推荐系统 [11]：推荐系统的组成、场景转化指标（pv点击率,uv点击率,曝光点击率）、用户数据指标等评价指标详解'}
