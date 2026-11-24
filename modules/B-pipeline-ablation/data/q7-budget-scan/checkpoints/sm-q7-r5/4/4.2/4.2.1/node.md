# N69: HDD层400TB冷数据的RAID6/EC重建瓶颈带宽为单盘持续写入速度，典型企业级7200rpm HDD顺序写入带宽约为150-200 MB/s/盘（非100

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20, N21, N22

## Claim

HDD层400TB冷数据的RAID6/EC重建瓶颈带宽为单盘持续写入速度，典型企业级7200rpm HDD顺序写入带宽约为150-200 MB/s/盘（非100MB/s），需根据具体盘型修正

## Corrected Claim

HDD层400TB冷数据的RAID6/EC重建瓶颈带宽为单盘持续写入速度，典型企业级7200rpm HDD顺序写入带宽约为150-200 MB/s/盘（非100MB/s），需根据具体盘型修正

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在概念重叠和逻辑包含关系。子节点1提供了基准带宽区间（150-200 MB/s），子节点2在此基础上引入了衰减系数（80-90%）并得出了实际有效带宽（120-180 MB/s）。子节点2的内容实际上是对子节点1参数的进一步修正和细化，两者并非独立的正交维度，而是同一参数（有效写入带宽）的不同计算阶段或视角，导致信息冗余。）

## Search Query

enterprise HDD sequential write speed MB/s 7200rpm 2024
