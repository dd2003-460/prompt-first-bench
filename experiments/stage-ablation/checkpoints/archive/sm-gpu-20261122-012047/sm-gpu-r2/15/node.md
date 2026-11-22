# N177: 所有标注为 [待核验] 的价格数据（如 B200, MI325X, H100 实际采购价）均基于 2024 Q4-2025 Q1 的市场传闻或分析师预测，非实时

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

所有标注为 [待核验] 的价格数据（如 B200, MI325X, H100 实际采购价）均基于 2024 Q4-2025 Q1 的市场传闻或分析师预测，非实时成交价；最终 TCO 计算需在执行前通过至少两家供应商获取实时报价进行修正，误差范围预计 ±15%。

## Corrected Claim

所有标注为 [待核验] 的价格数据（如 B200, MI325X, H100 实际采购价）可能基于特定时间窗口的市场传闻或分析师预测，非实时成交价；最终 TCO 计算需在执行前通过至少两家供应商获取实时报价进行修正。

## Evidence

[质询]该陈述包含具体的经验性预测（误差范围±15%）和特定时间窗口的市场状态描述（2024 Q4-2025 Q1），这些属于经验事实，无法从第一性原理推导，且参考来源主要提供实时或历史租赁价格数据，未直接证实该特定时间窗口的传闻性质及具体的误差幅度。 | 逻辑自洽，但参考来源[1][2][3]主要提供实时或统计租赁价格，未直接支持‘2024 Q4-2025 Q1基于传闻’及‘±15%误差’这一具体经验性结论，属于经验事实缺来源直接支持。

## Retrieval Sources

- {'url': 'https://gputracker.dev/gpu-cloud-statistics-2026&rut=2b7c71fae8a7a28ce32a6d9063756d0be84719b4555dcffd83182c186f8d45ec', 'type': 'ddg', 'title': 'GPU Cloud Statistics 2026: 50+ Citable Stats on H100, H200, B200 ...'}
- {'url': 'https://data.ornn.com/markets&rut=dc8db72d2eff42976072c23e23d53486300ffa18111ae72f3dcc8b7e25954f75', 'type': 'ddg', 'title': 'GPU Price Index: Daily H100, H200, B200 & A100 Rental Prices | Ornn'}
- {'url': 'https://www.ai-club.cn/compute/gpu-rental&rut=94399f48d098afc532afcbc970c527da7430498d9ee9b69f381b01cd9603a18c', 'type': 'ddg', 'title': 'Gpu租用价格实时对比：H100/B200/A100 各云厂商报价（每3小时更新）'}
