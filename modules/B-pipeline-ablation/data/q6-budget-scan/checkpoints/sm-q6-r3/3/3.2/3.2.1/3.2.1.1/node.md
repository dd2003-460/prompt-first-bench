# N201: 紧凑部署工作点（1机柜）：假设 N_servers=10 台 1U 服务器，每机柜容纳 12 台，则 N_racks = ceil(10/12) = 1 个机柜

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

紧凑部署工作点（1机柜）：假设 N_servers=10 台 1U 服务器，每机柜容纳 12 台，则 N_racks = ceil(10/12) = 1 个机柜，最小化机房租赁面积和电力分摊，但散热冗余较低。

## Corrected Claim

紧凑部署工作点（1机柜）：假设 N_servers=10 台 1U 服务器，每机柜容纳 12 台，则 N_racks = ceil(10/12) = 1 个机柜，最小化机房租赁面积和电力分摊，但散热冗余较低。

## Evidence

先验知识/题面给定，逻辑校验通过：10台服务器除以每机柜12台的容量，向上取整确实为1个机柜，数学推导正确且符合数据中心部署常识。

## Search Query

42U rack 1U server capacity density
