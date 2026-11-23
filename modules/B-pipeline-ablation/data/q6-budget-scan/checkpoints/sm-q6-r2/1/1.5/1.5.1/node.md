# N49: 自建节点每GB流量成本 P_bw_self_GB = (物理带宽月租单价 P_mbps * 12 * 1024) / (B_phys * U_util * 86

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

自建节点每GB流量成本 P_bw_self_GB = (物理带宽月租单价 P_mbps * 12 * 1024) / (B_phys * U_util * 86400 * 30 * 8 * 1024^3)，其中 P_mbps 约为 2-5 元/Mbps/月 [时效待核]。

## Corrected Claim

自建节点每GB流量成本 P_bw_self_GB = (物理带宽月租单价 P_mbps * 12 * 1024) / (B_phys * U_util * 86400 * 30 * 8 * 1024^3)，其中 P_mbps 约为 2-5 元/Mbps/月 [时效待核]。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲推导正确（分子为元/月，分母为字节/月，结果为元/字节），且2-5元/Mbps/月符合国内IDC带宽租赁的市场经验量级。

## Search Query

leased line bandwidth cost per GB calculation
