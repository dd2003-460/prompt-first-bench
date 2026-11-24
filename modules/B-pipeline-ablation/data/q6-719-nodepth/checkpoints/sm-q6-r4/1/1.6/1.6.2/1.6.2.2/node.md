# N198: TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS 协商（Server 直接返回 ChangeCipherSpec 和 Finished），加上 TCP 1 RTT，总连接延迟为 2 RTT。

## Corrected Claim

TLS 1.2 会话恢复（Session Resumption）使用 Session ID 或 Session Ticket 时，只需 1 RTT 完成 TLS 协商（Server 直接返回 ChangeCipherSpec 和 Finished），加上 TCP 1 RTT，总连接延迟为 2 RTT。

## Evidence

父节点级核验未通过：不完备（子节点1和2分别详细阐述了Session ID和Session Ticket两种模式的技术细节（状态/无状态、开销），子节点3阐述了握手过程的延迟构成。三者主题不同，互不重叠，正交性良好。然而，父节点核心结论是“总连接延迟为 2 RTT”（TLS 1 RTT + TCP 1 RTT），但子节点中完全没有涉及 TCP 握手（TCP 1 RTT）这一关键组成部分，导致对父节点结论的支撑不完备。）
