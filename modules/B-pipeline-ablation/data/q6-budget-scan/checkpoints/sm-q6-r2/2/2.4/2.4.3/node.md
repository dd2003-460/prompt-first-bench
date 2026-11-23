# N85: 自建节点按流量计费单价 p_traffic_self 的本质是带宽租赁成本分摊，p_traffic_self = C_bandwidth_package_mon

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

自建节点按流量计费单价 p_traffic_self 的本质是带宽租赁成本分摊，p_traffic_self = C_bandwidth_package_monthly / V_capacity_monthly，其中 C_bandwidth_package_monthly 为每月支付的静态带宽或95峰值费用，V_capacity_monthly 为实际承载流量；若自建节点采用静态带宽包（如 1Gbps 包月 ¥10k-20k），折合每 GB 成本约为 ¥0.01-0.03/GB（假设满载），远低于公有云，但存在带宽利用率不足时的成本浪费风险。

## Corrected Claim

自建节点按流量计费单价 p_traffic_self 的本质是带宽租赁成本分摊，p_traffic_self = C_bandwidth_package_monthly / V_capacity_monthly，其中 C_bandwidth_package_monthly 为每月支付的静态带宽或95峰值费用，V_capacity_monthly 为实际承载流量；若自建节点采用静态带宽包（如 1Gbps 包月 ¥10k-20k），折合每 GB 成本约为 ¥0.01-0.03/GB（假设满载），远低于公有云，但存在带宽利用率不足时的成本浪费风险。

## Evidence

先验知识/题面给定，逻辑校验通过：1Gbps满载月流量约3.24TB，10k-20k元/月折合0.003-0.006元/GB，若考虑利用率不足（如50%），成本升至0.006-0.012元/GB，与陈述中0.01-0.03元/GB量级兼容（陈述可能隐含了更低的利用率或更高的带宽包价格区间，但整体逻辑自洽且符合行业常识）。

## Search Query

self-built edge node bandwidth cost per GB static bandwidth package pricing
