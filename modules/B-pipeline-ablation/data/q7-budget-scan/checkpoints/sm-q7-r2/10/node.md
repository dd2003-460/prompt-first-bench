# N38: 本地 NVMe SSD 阵列的电力成本：NVMe SSD 功耗约 6-8W/盘，500TB 需约 50-100 块盘，加上服务器主板、CPU、内存、网络，单节点

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点之间存在严重的逻辑依赖和计算冗余。子节点2基于子节点1修正后的单节点功耗进行总功耗推导，子节点3又基于子节点2的结果计算电费。这种线性推导链条导致子节点并非正交（独立）的维度，而是同一计算流程的不同步骤。此外，子节点1和2中关于功耗参数的修正存在重复描述，且最终电费结果（¥21,677）落在父节点原始估算区间（¥16,000-25,000）内，说明分解主要是在验证/微调同一参数，而非探索独立的关键方面。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29194693/article/details/168510174&rut=e045f898195bf64e532662b166bef5fccfdb3ffa675e13bd23dcaa07aa45a540', 'type': 'ddg', 'title': 'NVMe SSD自适应功耗优化：APST机制、算法设计与固件实践-CSDN博客'}
- {'url': 'https://blog.csdn.net/zhuzongpeng/article/details/156773768&rut=099989ac7de11637a50ee5afb4445d1612288f31da9f345eb211d684226d633b', 'type': 'ddg', 'title': 'NVMe SSD自适应功耗优化_nmve硬盘功耗-CSDN博客'}
- {'url': 'https://ngabbs.com/read.php?tid=25315011&rut=b434d288e845537cde4f839ddea9af3a2049aceff568ea377e089eb361a0be3b', 'type': 'ddg', 'title': '11款市售主流nvme Ssd详细性能及功耗详细横评 [我是搬运工] Nga玩家社区'}
