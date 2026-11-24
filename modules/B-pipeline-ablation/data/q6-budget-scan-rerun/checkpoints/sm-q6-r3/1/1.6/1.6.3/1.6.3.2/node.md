# N160: 三线城市公有云CDN P99延迟构成公式：Latency_P99_3rd = RTT_Origin_to_3rd + T_processing + T_queu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

三线城市公有云CDN P99延迟构成公式：Latency_P99_3rd = RTT_Origin_to_3rd + T_processing + T_queueing，其中RTT_Origin_to_3rd需基于主要运营商骨干网延迟数据（通常15-30ms）及边缘节点距离校准，若边缘节点未覆盖三线，则RTT显著增加至50-80ms。

## Corrected Claim

三线城市公有云CDN P99延迟构成公式：Latency_P99_3rd = RTT_Origin_to_3rd + T_processing + T_queueing，其中RTT_Origin_to_3rd需基于主要运营商骨干网延迟数据（通常15-30ms）及边缘节点距离校准，若边缘节点未覆盖三线，则RTT显著增加至50-80ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

China Tier 3 city internet latency to major CDN PoPs average RTT
