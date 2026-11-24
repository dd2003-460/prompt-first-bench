# N720: 将核心区域扩展至一线+新一线+强二线（共 15-20 个城市）时，P_core 的估算值为 45.0%-50.0%。计算依据：一线 23.5% + 新一线 22

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N239

## Claim

将核心区域扩展至一线+新一线+强二线（共 15-20 个城市）时，P_core 的估算值为 45.0%-50.0%。计算依据：一线 23.5% + 新一线 22.5% + 强二线（苏州、东莞、佛山、宁波、青岛、合肥、福州、厦门）约 15.0% = 61.0%，但考虑到部分强二线用户已计入新一线统计口径或存在重叠，保守估计去重后约为 48.0%。

## Corrected Claim

将核心区域扩展至一线+新一线+强二线（共 15-20 个城市）时，P_core 的估算值约为 45.0%-50.0%（基于一线 23.5%、新一线 22.5%、强二线约 15.0% 的加总并保守去重后的估计，具体数值依赖于特定的用户统计口径和去重规则）。

## Evidence

[质询]该陈述涉及特定城市层级（一线、新一线、强二线）的用户占比统计及去重逻辑，属于经验性市场数据。参考来源均为英特尔CPU技术文档，与该市场统计事实完全无关，无法提供外部支持。此外，'强二线'的定义及具体城市列表（如是否包含苏州、东莞等）在不同统计口径下存在差异，且'部分强二线用户已计入新一线统计口径'这一去重假设缺乏数据支撑，存在口径混淆风险。 | 参考来源[1][2][3]均讨论Intel Xeon 6 P-core/E-core技术，与城市用户占比统计无关，无可用外部证据。该事实为经验数据，逻辑上算术自洽（23.5+22.5+15=61，去重后48），但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

China strong second-tier cities mobile user share Suzhou Dongguan Foshan Ningbo 2023

## Retrieval Sources

- {'url': 'https://post.smzdm.com/p/a5rvg9ok/&rut=8558e2e7627e2916140c6066fc973d100d39a5309702b47cff074958a2649c35', 'type': 'ddg', 'title': '至强6+和P-core怎么选？一张图看懂英特尔双线CPU的真正区别'}
- {'url': 'https://www.intel.cn/content/www/cn/zh/content-details/824430/2024-intel-tech-tour-next-gen-p-core-the-lion-cove-microarchitecture.html&rut=85adad76fda24dfcf6ace112bcb438f0d54051597e07815a2693fc03d590a1ad', 'type': 'ddg', 'title': '2024 年英特尔技术之旅：下一代 P 核 — Lion Cove 微架构'}
- {'url': 'https://blog.csdn.net/weixin_42570484/article/details/162675949&rut=bc4b0a666effa94fa307c567f165f4ae9e9fea21fcc7da81405fdc637702b188', 'type': 'ddg', 'title': 'Intel Xeon 6 处理器选型指南：P-core与E-core 4大应用场景性能对比-CSDN博客'}
