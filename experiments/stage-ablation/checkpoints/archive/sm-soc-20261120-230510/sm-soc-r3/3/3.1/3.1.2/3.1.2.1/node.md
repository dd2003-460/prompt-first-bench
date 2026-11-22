# N182: CTR_base（基准点击率）的量化：定义为 P_ask = P_median 且无促销标签时的平台平均点击率，典型值需基于特定品类历史数据（如 3%-8%）确

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N56

## Claim

CTR_base（基准点击率）的量化：定义为 P_ask = P_median 且无促销标签时的平台平均点击率，典型值需基于特定品类历史数据（如 3%-8%）确定，作为 f() 函数的截距项。

## Corrected Claim

CTR_base（基准点击率）定义为无促销标签时的平台平均点击率，作为 f() 函数的截距项；其典型值需基于特定品类历史数据确定（常见范围可能在 1%-10% 之间，具体视品类而定）。

## Evidence

[质询]陈述中给出的具体数值范围（3%-8%）属于经验事实，且高度依赖特定品类、平台及时间窗口，缺乏通用性；仅凭逻辑无法确定该具体区间，需依赖特定数据集验证。 | 来源[1]仅讨论CTR建模的一般性概念，未提供具体的基准点击率数值范围（3%-8%）或特定定义（P_ask=P_median），属于间接相关但无直接数值支持；该数值为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

e-commerce marketplace average CTR median price baseline category specific

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/372048174&rut=3cb6d900d4d086bec6317a557f91ae3c36b136e4d2f229d246beda91723f040d', 'type': 'ddg', 'title': '你真的懂点击率 (Ctr)建模吗？ - 知乎'}
