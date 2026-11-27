# N146: 买家筛选成本 C_filter 定义为在信息质量 info_quality 约束下，买家为识别商品真实价值 V_true 需浏览的商品数量 N_view 的期望

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

买家筛选成本 C_filter 定义为在信息质量 info_quality 约束下，买家为识别商品真实价值 V_true 需浏览的商品数量 N_view 的期望值，公式为 C_filter = N_view * c_time，其中 N_view 与噪声方差 σ_noise² 呈正相关，具体弹性系数需通过 A/B 测试中不同信息透明度下的浏览深度数据回归获得。

## Corrected Claim

在特定的信息不对称市场模型中，买家筛选成本 C_filter 可定义为在信息质量约束下，买家为识别商品真实价值需浏览的商品数量 N_view 的期望值乘以单位浏览时间成本 c_time，即 C_filter = N_view * c_time；其中 N_view 通常与噪声方差正相关，具体弹性系数需通过实证数据（如 A/B 测试）回归获得。

## Evidence

[质询]该陈述属于特定经济/信息模型中的定义性假设，缺乏通用性；且参考来源均为数据库/网络工具中的'CFilter'函数，与经济学中的'筛选成本'概念完全无关，存在严重的术语混淆风险。 | 逻辑上自洽（成本=数量*单位时间成本，噪声大导致需浏览更多商品），但参考来源[1][2][3]均涉及数据库或网络过滤工具，与该经济学事实主题无关，无外部证据支持，且作为经验/模型设定事实，缺乏来源直接支持。

## Search Query

second hand marketplace buyer search cost information asymmetry browsing depth elasticity

## Retrieval Sources

- {'url': 'https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/Database-Analytic-Functions/Association-Analysis-Functions/TD_CFilter&rut=16c337e4ab380cf66dea0ee82837008b87ab9131b2b9c079b0fe3c3728d50f7e', 'type': 'ddg', 'title': 'TD_CFilter | CFilter | Teradata Vantage - TD_CFilter - Analytics Database'}
- {'url': 'https://blog.csdn.net/gitblog_00912/article/details/153549542&rut=5705ea58a5df09316032a025b2db56b8d7f323336b8f2a8b5b5cdc14f04391cf', 'type': 'ddg', 'title': '如何用cfilter优化数据库查询？5分钟上手Go语言布谷鸟过滤器-CSDN博客'}
- {'url': 'https://blog.csdn.net/tskyfree/article/details/41219899&rut=e8a4299c49d69b4044c89ad90e3b9d80f16892f41649949681713cc25c010ca1', 'type': 'ddg', 'title': 'wireshark过滤语法总结_wireshark info过滤-CSDN博客'}
