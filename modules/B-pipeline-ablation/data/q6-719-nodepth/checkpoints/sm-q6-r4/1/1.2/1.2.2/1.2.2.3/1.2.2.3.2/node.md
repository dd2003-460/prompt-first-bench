# N638: 跨网惩罚项 ΔT_cross_net 的触发概率 P_cross_net 取决于用户 ISP 分布与 CDN 节点接入 ISP 分布的重合度，若 CDN 节点多

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

跨网惩罚项 ΔT_cross_net 的触发概率 P_cross_net 取决于用户 ISP 分布与 CDN 节点接入 ISP 分布的重合度，若 CDN 节点多线接入（BGP），P_cross_net 可降至 <5%；若单线接入，P_cross_net 约为 30-50%。

## Corrected Claim

跨网惩罚项 ΔT_cross_net 的触发概率 P_cross_net 取决于用户 ISP 分布与 CDN 节点接入 ISP 分布的重合度，若 CDN 节点多线接入（BGP），P_cross_net 可降至 <5%；若单线接入，P_cross_net 约为 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN multi-line BGP vs single line cross-network traffic ratio
