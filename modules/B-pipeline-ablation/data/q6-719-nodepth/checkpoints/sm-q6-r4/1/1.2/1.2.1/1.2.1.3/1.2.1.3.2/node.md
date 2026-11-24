# N631: 回源传输时间 T_transfer 的精确计算公式：T_transfer = (s_weighted * 8 * 1024^3) / (B_origin * 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

回源传输时间 T_transfer 的精确计算公式：T_transfer = (s_weighted * 8 * 1024^3) / (B_origin * 10^9 * η_eff) + T_handshake_origin，其中 η_eff 为网络有效利用率（通常 0.8-0.9），T_handshake_origin 为源站 TLS/HTTP 握手延迟（通常 5-10ms）。

## Corrected Claim

回源传输时间 T_transfer 的精确计算公式：T_transfer = (s_weighted * 8 * 1024^3) / (B_origin * 10^9 * η_eff) + T_handshake_origin，其中 η_eff 为网络有效利用率（通常 0.8-0.9），T_handshake_origin 为源站 TLS/HTTP 握手延迟（通常 5-10ms）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（字节转比特除以带宽），参数取值范围（η_eff 0.8-0.9, 握手 5-10ms）符合网络工程常识。

## Search Query

data transfer time calculation formula network efficiency handshake latency
