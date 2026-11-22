# N216: NVLink 4.0 (H100) 的单卡互联带宽为 900 GB/s，但 TP=2 通信路径涉及两个方向的数据交换，实际有效带宽受限于链路利用率，通常取理论值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

NVLink 4.0 (H100) 的单卡互联带宽为 900 GB/s，但 TP=2 通信路径涉及两个方向的数据交换，实际有效带宽受限于链路利用率，通常取理论值的 85-90% 进行保守估计。

## Corrected Claim

NVLink 4.0 (H100) 的单卡互联带宽为 900 GB/s，但 TP=2 通信路径涉及两个方向的数据交换，实际有效带宽受限于链路利用率，通常取理论值的 85-90% 进行保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 NVLink 4.0 总带宽确为 900 GB/s，TP=2 双向通信及 85-90% 利用率估算符合工程常识。
