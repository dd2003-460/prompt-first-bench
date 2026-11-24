# N69: HDD层400TB冷数据的RAID6/EC重建瓶颈带宽为单盘持续写入速度，典型企业级7200rpm HDD顺序写入带宽约为150-200 MB/s/盘（非100

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（两个子节点分别定义了‘标称理论上限’和‘实际有效带宽’，逻辑层级清晰且互斥，共同构成了对父节点中‘瓶颈带宽’的完整量化描述，无重复或矛盾。）

## Search Query

enterprise HDD sequential write speed MB/s 7200rpm 2024
