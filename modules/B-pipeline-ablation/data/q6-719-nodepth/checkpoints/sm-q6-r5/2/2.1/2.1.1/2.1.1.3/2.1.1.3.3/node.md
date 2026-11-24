# N491: C_max 与 L_queue_wait 的耦合效应：当 C_current 接近 C_max 时，内核 TCP 握手队列溢出，导致 L_queue_wait 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N157

## Claim

C_max 与 L_queue_wait 的耦合效应：当 C_current 接近 C_max 时，内核 TCP 握手队列溢出，导致 L_queue_wait 包含连接建立延迟 L_conn_estab ≈ 1-2 RTT；对于 100 ms RTT，L_conn_estab ≈ 200 ms，远超应用层队列等待，需监控 TCP 三次握手成功率以检测此瓶颈。

## Corrected Claim

C_max 与 L_queue_wait 的耦合效应：当 C_current 接近 C_max 时，内核 TCP 握手队列溢出，导致 L_queue_wait 包含连接建立延迟 L_conn_estab ≈ 1-2 RTT；对于 100 ms RTT，L_conn_estab ≈ 200 ms，远超应用层队列等待，需监控 TCP 三次握手成功率以检测此瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP握手队列溢出导致连接建立延迟（约1-2 RTT）是内核网络栈的标准行为，100ms RTT对应200ms延迟符合物理直觉，且监控握手成功率是检测此类瓶颈的标准手段。
