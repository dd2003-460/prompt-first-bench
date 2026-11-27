# N134: 异质性偏好方差 σ²_preference 的量化：σ²_preference = σ²_wtp，其中 σ²_wtp 为买家对同类商品支付意愿（WTP）的总体方

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

异质性偏好方差 σ²_preference 的量化：σ²_preference = σ²_wtp，其中 σ²_wtp 为买家对同类商品支付意愿（WTP）的总体方差，需通过买家出价分布或搜索行为数据估计。

## Corrected Claim

在仅考虑价格异质性的简化模型中，异质性偏好方差可近似为支付意愿（WTP）的总体方差 σ²_wtp；但在一般情形下，偏好方差应包含多维属性偏好的综合方差，需通过多维数据估计。

## Evidence

[质询]该陈述将异质性偏好方差直接等同于支付意愿（WTP）的总体方差，忽略了偏好可能包含非价格维度（如质量、品牌、属性等），且WTP方差受收入分布影响，不一定能完全代表偏好异质性；此外，来源[2]摘要乱码无法提供有效支持，来源[1]虽涉及偏好建模但未明确给出该等式。 | 逻辑上在纯价格竞争模型中自洽，但作为一般性定义过于简化；来源[1]间接相关但未直接支持该等式，来源[2]不可读，缺乏直接外部证据支持该具体量化公式。

## Search Query

variance of willingness to pay distribution second-hand market buyer behavior data

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2507.13541&rut=a9c14c501fe29081f970a8c34d2f41f9d209497734d50073f86f9ead02cc3ab2', 'type': 'ddg', 'title': '[2507.13541] PrefPalette: Personalized Preference Modeling with Latent ...'}
- {'url': 'https://www.nsd.pku.edu.cn/attachments/4f8dad0a6d874a5fbfcb972156d6e913.pdf&rut=17ceb774790efaa7774d68f0a009184ff90cb1cd1af79cd58428c276cbf129d8', 'type': 'ddg', 'title': 'PDF 异质性财 - nsd.pku.edu.cn'}
