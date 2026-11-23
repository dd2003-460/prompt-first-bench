# N211: 系统开销 T_overhead 的网络与协议栈成本：T_overhead = T_tcp_handshake + T_tls_handshake + T_ker

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

系统开销 T_overhead 的网络与协议栈成本：T_overhead = T_tcp_handshake + T_tls_handshake + T_kernel_processing，对于 HTTP/1.1 新建连接，T_tcp+tls ≈ 1-3 RTT (10-30ms)；对于 HTTP/2 多路复用或 Keep-Alive 长连接，T_overhead 降至 0.1-0.5 ms (仅内核协议栈处理与 TCP/IP 封装开销)

## Corrected Claim

系统开销 T_overhead 的网络与协议栈成本：T_overhead = T_tcp_handshake + T_tls_handshake + T_kernel_processing，对于 HTTP/1.1 新建连接，T_tcp+tls ≈ 1-3 RTT (10-30ms)；对于 HTTP/2 多路复用或 Keep-Alive 长连接，T_overhead 降至 0.1-0.5 ms (仅内核协议栈处理与 TCP/IP 封装开销)

## Evidence

先验知识/题面给定，逻辑校验通过：TCP+TLS握手耗时与RTT线性相关，长连接复用消除握手开销仅留内核处理，量级符合网络协议栈常识。
