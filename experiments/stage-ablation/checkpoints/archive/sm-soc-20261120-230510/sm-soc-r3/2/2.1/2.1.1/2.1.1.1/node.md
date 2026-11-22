# N145: CTR均值 μ_ctr 对价格偏离的边际敏感度：在基准价格 P_median 附近，每增加 1% 的挂价偏离 (P_ask/P_median - 1)，CTR 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N44

## Claim

CTR均值 μ_ctr 对价格偏离的边际敏感度：在基准价格 P_median 附近，每增加 1% 的挂价偏离 (P_ask/P_median - 1)，CTR 下降约 0.5%-1.5%（基于电商搜索点击率弹性研究），即 ∂μ_ctr/∂(P_dev) ∈ [-0.015, -0.005]。

## Corrected Claim

在基准价格附近，挂价偏离对CTR的边际敏感度通常为负值，具体弹性系数需依据特定电商场景的实证数据确定，一般认为价格上升会显著降低点击率。

## Evidence

[质询]该陈述声称基于“电商搜索点击率弹性研究”，但提供的参考来源均为“广告CTR校准/建模”技术文章，领域不匹配（广告竞价 vs 电商搜索/挂价），且来源中未包含任何关于价格偏离对CTR边际敏感度的具体数值或弹性系数，属于经验事实缺乏直接来源支持。 | 参考来源[1][2][3]均聚焦于广告pCTR校准与建模，未涉及电商搜索场景下价格偏离对CTR的具体弹性数值，无法提供直接支持；该数值属于经验事实，逻辑上量级合理（价格上升导致点击率下降），但缺乏来源验证。

## Search Query

second hand marketplace CTR price elasticity click through rate vs asking price deviation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42527401/article/details/167426709&rut=5c405ae157c3ffdff268aac0ed1c2b834d64ce336548c888c88206fed33d1633', 'type': 'ddg', 'title': '广告ctr校准工程实践：从sir到mbct的工业级概率修正路径-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_29042035/article/details/170886745&rut=b2472b937f38cbdd17633525b5c890f529d6eca5120ff7f35b78dc3696374149', 'type': 'ddg', 'title': '广告点击率校准技术全解析：从sir到pccem的工业级演进-csdn博客'}
- {'url': 'https://cloud.tencent.com/developer/article/1890590&rut=e612d197766d3075d5904fa20b7dbedc20341181d23bdef670ebf6dcc6fb902f', 'type': 'ddg', 'title': '一文搞懂ctr建模-腾讯云开发者社区-腾讯云'}
