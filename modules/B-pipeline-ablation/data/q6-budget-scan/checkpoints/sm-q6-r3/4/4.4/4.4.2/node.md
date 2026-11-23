# N138: 跨域回源握手延迟 $RTT_{handshake}$ 的构成：$RTT_{handshake} = N_{rtt} \cdot RTT_{prop}(D_{cr

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

跨域回源握手延迟 $RTT_{handshake}$ 的构成：$RTT_{handshake} = N_{rtt} \cdot RTT_{prop}(D_{cross}) + T_{process}$，其中 $N_{rtt}$ 为 TCP/TLS 握手往返次数（TCP+TLS1.3 通常为 1-2 RTT，TLS1.2 为 2 RTT），$T_{process}$ 为源站处理开销（<5ms），典型值为 20-60 ms。

## Corrected Claim

跨域回源握手延迟 $RTT_{handshake}$ 的构成：$RTT_{handshake} = N_{rtt} \cdot RTT_{prop}(D_{cross}) + T_{process}$，其中 $N_{rtt}$ 为 TCP/TLS 握手往返次数（TCP+TLS1.3 通常为 1-2 RTT，TLS1.2 为 2 RTT），$T_{process}$ 为源站处理开销（<5ms），典型值为 20-60 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP+TLS1.3握手确实可压缩至1-2 RTT，TLS1.2为2 RTT，源站处理开销<5ms及总延迟20-60ms的量级符合跨域网络传输的工程常识。
