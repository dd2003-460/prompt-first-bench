# N294: 本地工作站/小型数据中心场景下的有效 PUE (Power Usage Effectiveness) 通常高于大型云数据中心（1.1-1.2），因缺乏集中制冷和

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

本地工作站/小型数据中心场景下的有效 PUE (Power Usage Effectiveness) 通常高于大型云数据中心（1.1-1.2），因缺乏集中制冷和冗余电源，估算值为 1.3-1.5；若 PUE 取 1.4，则年电费修正系数从 0.9 变为 1.4，导致年电费从 1,942 元上升至 3,002 元。

## Corrected Claim

本地工作站/小型数据中心场景下的有效 PUE (Power Usage Effectiveness) 通常高于大型云数据中心（1.1-1.2），因缺乏集中制冷和冗余电源，估算值为 1.3-1.5；若 PUE 取 1.4，则年电费修正系数从 0.9 变为 1.4，导致年电费从 1,942 元上升至 3,002 元。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE 1.3-1.5 符合小型数据中心缺乏集中制冷的工程常识；数学计算 1942 * (1.4/0.9) ≈ 3002 准确无误。
