# N11: 单卡方案 TCO 中的硬件采购成本为显卡市场价，需对比 RTX 4090/5090、A100、H100、MI300X 等主流卡的价格区间（美元），数据需标注时效

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

单卡方案 TCO 中的硬件采购成本为显卡市场价，需对比 RTX 4090/5090、A100、H100、MI300X 等主流卡的价格区间（美元），数据需标注时效性

## Corrected Claim

单卡方案 TCO 分析中，硬件采购成本通常基于显卡市场参考价，需对比 RTX 4090/5090、A100、H100、MI300X 等主流卡的价格区间（美元），并标注数据时效性以反映市场波动。

## Evidence

[质询]该陈述是一个方法论/任务描述，而非具体的经验事实数值。其潜在错误在于隐含假设“硬件采购成本=显卡市场价”在单卡方案中是绝对准确的，忽略了渠道溢价、批量折扣或二手市场波动等现实因素，且未提供具体的价格区间数据，仅作为待执行的任务节点，缺乏可验证的具体事实内容。 | 来源[1]和[2]直接支持TCO分析中需包含采购成本及对比不同GPU（如4090）的方法论，但来源未提供RTX 5090、A100、H100、MI300X的具体价格区间数据，且该节点为任务描述而非事实陈述，故降级为定性表述。

## Search Query

RTX 4090 A100 H100 MI300X price USD 2024

## Retrieval Sources

- {'url': 'https://mirrorfrog.com/docs/tco-calculator/&rut=a019aea46c535e1286e47e046d30737a5ab0ccc79908da03912a5e532b166141', 'type': 'ddg', 'title': 'Ai 算力卡 Tco 计算器 | 总体拥有成本分析 | Ai 算力卡百科 | 252 款 Ai 芯片规格对比'}
- {'url': 'https://segmentfault.com/a/1190000048037779&rut=a90f444cde48faf69a662e4695466b9a675e188b47e66fd41a27d8cea9f46265', 'type': 'ddg', 'title': '企业GPU算力采购避坑指南：TCO五维拆解与3个真实成本案例 - 个人文章 - SegmentFault 思否'}
- {'url': 'https://post.smzdm.com/p/awwpozlg/&rut=e41bada3e0d8f2d4840a567fb2dc728463c2f3ea6cb5eb8d82ca4f3fe4a2b8f4', 'type': 'ddg', 'title': 'Rtx 4090买还是租？三年成本差27万，这份实测指南说透了'}
