# N486: 负载率 L_util 的动态计算：L_util = (Current_Requests_Per_Sec / Max_Requests_Per_Sec) * 10

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N156

## Claim

负载率 L_util 的动态计算：L_util = (Current_Requests_Per_Sec / Max_Requests_Per_Sec) * 100%，其中 Max_Requests_Per_Sec 由单节点压测得出（如 5000 QPS）；需结合 N25 的流量波动系数 K_t，在峰值时段 L_util_peak = L_util_avg * K_peak，若 K_peak = 4 且 L_util_avg = 60%，则 L_util_peak = 240%（触发过载保护）。

## Corrected Claim

负载率 L_util 的动态计算：L_util = (Current_Requests_Per_Sec / Max_Requests_Per_Sec) * 100%，其中 Max_Requests_Per_Sec 由单节点压测得出（如 5000 QPS）；需结合 N25 的流量波动系数 K_t，在峰值时段 L_util_peak = L_util_avg * K_peak，若 K_peak = 4 且 L_util_avg = 60%，则 L_util_peak = 240%（触发过载保护）。

## Evidence

先验知识/题面给定，逻辑校验通过：负载率定义符合工程惯例，峰值计算 60% * 4 = 240% 数学正确，过载保护逻辑自洽。
