# N44: 电力消耗细化模型：NVMe SSD空闲功耗约0.5W/TB，读写功耗约1.0W/TB；HDD空闲功耗约0.05W/TB，读写功耗约0.15W/TB。假设温数据每

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

电力消耗细化模型：NVMe SSD空闲功耗约0.5W/TB，读写功耗约1.0W/TB；HDD空闲功耗约0.05W/TB，读写功耗约0.15W/TB。假设温数据每日扫描2小时，冷数据无读写，加权平均功耗需按时间占比计算。

## Corrected Claim

电力消耗细化模型：NVMe SSD空闲功耗极低（如8TB通常<0.5W，约0.06W/TB），读写功耗较高（如8TB可达7-10W，约1.0W/TB）；HDD功耗数据需另行查证。假设温数据每日扫描2小时，冷数据无读写，加权平均功耗需按时间占比计算。

## Evidence

[质询]数值量级与来源存在显著偏差：来源[1]指出8TB SSD空闲功耗通常不到0.5W（即<0.0625W/TB），而陈述中NVMe SSD空闲功耗为0.5W/TB（8TB即4W），高出来源数据约8倍；此外，HDD功耗数据在来源中完全缺失，属于无源经验参数。 | 来源[1]与NVMe SSD空闲功耗数值矛盾（来源显示8TB<0.5W，陈述隐含8TB=4W），且未覆盖HDD数据；作为经验事实，缺乏多源一致支持，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2044188334226937772&rut=55e2ef406c27ca49b83a37a05a86836b137f4a9579ca752e1831abed276d511c', 'type': 'ddg', 'title': '8tb Ssd的功耗和发热对笔记本电脑续航影响大吗？ - 知乎'}
