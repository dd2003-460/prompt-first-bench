# N354: 流量倾斜的阈值效应：定义流量倾斜系数 T_boost = T_exposure_high / T_exposure_normal，当 Price_Premium

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

流量倾斜的阈值效应：定义流量倾斜系数 T_boost = T_exposure_high / T_exposure_normal，当 Price_Premium > θ_boost（如 10%）时，T_boost 从 1.0 跳升至 1.8；需通过分段回归验证 θ_boost 的具体数值及跳变幅度。

## Corrected Claim

流量倾斜可能存在阈值效应：定义流量倾斜系数 T_boost = T_exposure_high / T_exposure_normal，当 Price_Premium 超过特定阈值 θ_boost 时，T_boost 可能显著上升；具体阈值及跳变幅度需通过分段回归等实证方法验证。

## Evidence

[质询]该陈述包含具体的经验性数值（阈值10%、跳变幅度1.8），属于电商/推荐系统领域的经验事实，无法从第一性原理推导，且参考来源完全无关，缺乏直接证据支持。 | 逻辑自洽（分段回归验证阈值效应是标准统计方法），但参考来源[1][2][3]分别涉及账号绑定、电力电子Boost变换器、气象集合预报，均与流量倾斜/价格溢价无关，无可用外部证据支持具体数值。

## Search Query

platform algorithm exposure threshold price premium jump

## Retrieval Sources

- {'url': 'https://d.wanfangdata.com.cn/thesis/ChhUaGVzaXNOZXdTMjAyNDA5MjAxNTE3MjUSCUQwMzQ5MzEwNRoIaXMyeWF6ZjE%3D&rut=6cdd5acb79117ee879677ef8c45e00e2d69979ca377ffed2359f0f96ee9154b5', 'type': 'ddg', 'title': '万方数据知识服务平台 - d.wanfangdata.com.cn'}
- {'url': 'https://blog.csdn.net/weixin_40318923/article/details/136426461&rut=333492100cb1ec2b15d231564bb96dd545e02213ff6b70b1180c64c397f41e3f', 'type': 'ddg', 'title': '【转载】手撕Boost!Boost公式推导及实验验证 - CSDN博客'}
- {'url': 'https://qxxb.cmsjournal.net/article/doi/10.11676/qxxb2026.20260014&rut=bfffe41f04be008ca2f3a314248a7ca98db1771c0f04761a37fd12fbfc2d98a9', 'type': 'ddg', 'title': 'CMA对流尺度集合随机物理倾向扰动参数敏感性研究'}
