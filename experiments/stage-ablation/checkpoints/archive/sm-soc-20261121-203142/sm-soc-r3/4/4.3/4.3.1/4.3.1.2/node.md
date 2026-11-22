# N200: 工作点2（中曝光-中成本）：假设降价触发权重微调，48小时内曝光量衰减系数 R_decay = 0.8，E_exp_new = 0.8 * E_exp_old，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

工作点2（中曝光-中成本）：假设降价触发权重微调，48小时内曝光量衰减系数 R_decay = 0.8，E_exp_new = 0.8 * E_exp_old，对应开发成本 C_dev = 10000元，适用于自然算法响应场景。

## Corrected Claim

工作点2（中曝光-中成本）：在假设降价触发权重微调的场景下，若设定48小时内曝光量衰减系数 R_decay 为 0.8，则新曝光量 E_exp_new 为旧曝光量的 0.8 倍；该场景对应的开发成本 C_dev 设定为 10000 元。

## Evidence

[质询]该陈述包含具体的经验性数值（衰减系数0.8、成本10000元、48小时窗口），这些属于特定业务场景下的假设参数或经验事实，无法从第一性原理推导，且参考来源均为ISP图像传感器自动曝光（AE）技术文档，与电商/算法运营中的“曝光量”及“开发成本”完全无关，存在严重的领域混淆风险。 | 参考来源[1][2][3]均讨论ISP硬件层面的自动曝光（AE）算法，与陈述中的业务运营指标（曝光量衰减、开发成本）主题完全无关，无可用外部证据支持；该陈述为特定场景下的假设参数，逻辑自洽但缺乏来源支持，依据经验事实排除条款降级。

## Search Query

Xianyu Zzhuan price reduction algorithm weight adjustment exposure decay 48 hours

## Retrieval Sources

- {'url': 'https://blog.csdn.net/sinat_28461591/article/details/148822532&rut=cae159f8d5adf7df1fbb036094441d915b42b7155a2e00c519c0a5a78457047f', 'type': 'ddg', 'title': '曝光矩阵与 Roi 区域权重配置策略：Ae 精准测光的核心机制'}
- {'url': 'https://bbs.csdn.net/weixin_32447969/article/details/100127216&rut=a764f3dd5c62230a4233b113d1411264303f2961da8d3e8f835e9eea8713a4f1', 'type': 'ddg', 'title': '别再只调曝光补偿了!ISP图像调试中，AE模块的权重、策略与收敛速度实战避坑指南'}
- {'url': 'https://blog.csdn.net/zzfmlxs/article/details/162965003&rut=1c8deeecb8972fe78fc04f775e347c0eaf04dac42982b73d5dc932510b751d71', 'type': 'ddg', 'title': '069、自动曝光（Ae）测光策略：全局/中心/点测光与曝光时间增益分配_高动态融合自动曝光策略-csdn博客'}
