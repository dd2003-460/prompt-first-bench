# N578: TLS 1.2 Session Resumption 的 1 RTT 握手过程中，服务器直接发送 ChangeCipherSpec 和 Finished 报文，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N198

## Claim

TLS 1.2 Session Resumption 的 1 RTT 握手过程中，服务器直接发送 ChangeCipherSpec 和 Finished 报文，其传输耗时 T_resumption_trans = (Size_CCS_Fin) / Effective_Bandwidth，通常小于 1ms，可忽略不计，主要延迟仍为 RTT

## Corrected Claim

TLS 1.2 Session Resumption 的 1 RTT 握手过程中，服务器直接发送 ChangeCipherSpec 和 Finished 报文，其传输耗时 T_resumption_trans = (Size_CCS_Fin) / Effective_Bandwidth，通常小于 1ms，可忽略不计，主要延迟仍为 RTT

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.2 会话恢复确实只需 1 RTT，服务器发送的 CCS 和 Finished 报文极小（通常 < 100 字节），在常规带宽下传输耗时微秒级，远小于 1ms，主要延迟确为 RTT。
