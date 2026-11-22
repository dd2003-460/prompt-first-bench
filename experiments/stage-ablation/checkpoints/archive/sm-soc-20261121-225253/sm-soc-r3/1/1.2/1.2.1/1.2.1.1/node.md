# N56: 买家价格敏感度方差 σ_buyer^2 的估计范围为 0.05-0.15，基于对同类商品成交价分布的变异系数（CV）推导，CV = σ/μ，其中 μ 为成交均价

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

买家价格敏感度方差 σ_buyer^2 的估计范围为 0.05-0.15，基于对同类商品成交价分布的变异系数（CV）推导，CV = σ/μ，其中 μ 为成交均价。

## Corrected Claim

买家价格敏感度方差的具体数值范围因商品类别和市场环境而异，不能简单通过同类商品成交价的变异系数（CV）统一推导为0.05-0.15；需结合具体的PSM调研数据或需求弹性模型进行估计。

## Evidence

[质询]该陈述声称基于“同类商品成交价分布的变异系数（CV）”推导得出买家价格敏感度方差，这在概念上存在混淆。成交价分布的离散程度（CV）反映的是市场交易价格的波动性或异质性，而“买家价格敏感度”通常指需求弹性或支付意愿的分布特征。虽然两者可能相关，但直接将成交价的CV等同于或简单推导为敏感度方差缺乏严格的经济学或统计学依据，且0.05-0.15这一具体数值范围缺乏通用性，高度依赖于特定商品类别，不能作为一个普适的估计范围。 | 参考来源[1]和[2]主要介绍PSM（价格敏感度测试）的问卷设计和原理，未提供关于“买家价格敏感度方差”的具体数值范围（0.05-0.15）或基于成交价CV推导该方差的方法论支持，属于经验事实且缺乏来源直接支持。

## Search Query

buyer price sensitivity variance second hand market transaction data analysis

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2601_96259506/article/details/162108071&rut=0f71e1acbc70d97d8049f56a3c3872626ff92310b186cbaa87d45c372ef9ee8f', 'type': 'ddg', 'title': '2026 PSM价格敏感度调研全指南：问卷设计、模型解读、工具推荐_问卷星设置psm价格题型收费吗-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_28709649/article/details/163456510&rut=3047d9c16645a73bfec6f836d300104263435dcc58f2a3a388c5794fa2d78349', 'type': 'ddg', 'title': '价格敏感度测试（Psm）实战指南：从原理到数据分析-csdn博客'}
