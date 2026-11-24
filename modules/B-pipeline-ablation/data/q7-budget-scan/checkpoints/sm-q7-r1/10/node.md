# N38: 本地 NVMe SSD 阵列的电力成本：NVMe SSD 功耗约 6-8W/盘，500TB 需约 50-100 块盘，加上服务器主板、CPU、内存、网络，单节点

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

本地 NVMe SSD 阵列的电力成本：NVMe SSD 功耗约 6-8W/盘，500TB 需约 50-100 块盘，加上服务器主板、CPU、内存、网络，单节点功耗约 500-800W。假设 3 节点集群，总功耗 1500-2400W。PUE=1.5，电价 ¥0.8/kWh，年电费 = (1500-2400W * 1.5 * 24h * 365d / 1000) * 0.8 ≈ ¥16,000-¥25,000/年。

## Corrected Claim

本地 NVMe SSD 阵列的电力成本估算：基于单节点功耗 500-800W 的假设（实际高密度存储节点可能更高），3 节点集群总功耗 1500-2400W，PUE=1.5，电价 ¥0.8/kWh，年电费约为 ¥16,000-¥25,000。

## Evidence

[质询]单节点功耗估算（500-800W）对于承载500TB NVMe存储的服务器而言可能偏低，通常此类高密度存储节点（含CPU、内存、多块NVMe及散热）功耗往往在1kW以上，导致总电费下限可能被低估；此外，500TB容量对应50-100块盘的假设依赖于具体的单盘容量（5-10TB），属于经验性假设而非固定事实。 | 来源[1][2][3]主要讨论NVMe SSD的功耗优化机制和单盘功耗测试，未提供服务器整机功耗、PUE或电价等系统级成本数据，无法直接支持最终电费结论；但计算逻辑自洽，属于经验事实估算，缺乏直接来源支持故降级。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29194693/article/details/168510174&rut=e045f898195bf64e532662b166bef5fccfdb3ffa675e13bd23dcaa07aa45a540', 'type': 'ddg', 'title': 'NVMe SSD自适应功耗优化：APST机制、算法设计与固件实践-CSDN博客'}
- {'url': 'https://blog.csdn.net/zhuzongpeng/article/details/156773768&rut=099989ac7de11637a50ee5afb4445d1612288f31da9f345eb211d684226d633b', 'type': 'ddg', 'title': 'NVMe SSD自适应功耗优化_nmve硬盘功耗-CSDN博客'}
- {'url': 'https://ngabbs.com/read.php?tid=25315011&rut=b434d288e845537cde4f839ddea9af3a2049aceff568ea377e089eb361a0be3b', 'type': 'ddg', 'title': '11款市售主流nvme Ssd详细性能及功耗详细横评 [我是搬运工] Nga玩家社区'}
