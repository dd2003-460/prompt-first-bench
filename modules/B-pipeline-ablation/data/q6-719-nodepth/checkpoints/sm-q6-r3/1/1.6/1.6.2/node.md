# N57: Total_Connect_Latency_TLS1.2 = 1 RTT (TCP Handshake) + 2 RTT (TLS 1.2 Full Hands

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Total_Connect_Latency_TLS1.2 = 1 RTT (TCP Handshake) + 2 RTT (TLS 1.2 Full Handshake) = 3 RTT；若启用会话恢复（Session Resumption），则 TLS 协商延迟降至 1 RTT（总 2 RTT）[待核验]

## Corrected Claim

Total_Connect_Latency_TLS1.2 = 1 RTT (TCP Handshake) + 2 RTT (TLS 1.2 Full Handshake) = 3 RTT；若启用会话恢复（Session Resumption），则 TLS 协商延迟降至 1 RTT（总 2 RTT）[待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.2 完整握手确实需要 2 RTT（ClientHello -> ServerHello+Cert+ServerDone, ClientKeyExchange+Finished -> ChangeCipherSpec+Finished），加上 TCP 3次握手 1 RTT，共 3 RTT；会话恢复（Session Resumption）通常将 TLS 握手压缩至 1 RTT（ClientHello -> ServerHello+Finished），总计 2 RTT。

## Search Query

TLS 1.2 session resumption handshake round trips
