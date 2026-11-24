# N326: TCP 握手延迟 T_tcp_handshake = 1 RTT (基础) + N_retrans * RTT (若丢包)，在 P99 场景下需假设丢包率 p_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

TCP 握手延迟 T_tcp_handshake = 1 RTT (基础) + N_retrans * RTT (若丢包)，在 P99 场景下需假设丢包率 p_loss，典型 p_loss < 0.1% 时 T_tcp ≈ 1 RTT。

## Corrected Claim

TCP 握手延迟 T_tcp_handshake = 1 RTT (基础) + N_retrans * RTT (若丢包)，在 P99 场景下需假设丢包率 p_loss，典型 p_loss < 0.1% 时 T_tcp ≈ 1 RTT。

## Evidence

先验知识/题面给定，逻辑校验通过
