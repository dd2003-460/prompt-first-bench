# N574: TLS 1.2 Full Handshake 第二个 RTT 的传输内容分解：ClientKeyExchange+Finished 与 Server Finis

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

TLS 1.2 Full Handshake 第二个 RTT 的传输内容分解：ClientKeyExchange+Finished 与 Server Finished 的报文大小及网络传输耗时 T_trans2 = (Size_CKE_Fin + Size_Srv_Fin) / Effective_Bandwidth

## Corrected Claim

TLS 1.2 Full Handshake 第二个 RTT 的传输内容分解：ClientKeyExchange+Finished 与 Server Finished 的报文大小及网络传输耗时 T_trans2 = (Size_CKE_Fin + Size_Srv_Fin) / Effective_Bandwidth

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.2 完整握手第二个 RTT 确实包含 ClientKeyExchange 和 Client Finished（客户端发送）以及 Server Finished（服务端发送），传输耗时公式符合物理直觉（总数据量除以有效带宽）。
