# N196: TLS 1.3 0-RTT (Early Data) 机制允许客户端在重连时发送应用数据与 ClientHello 一起，但服务器需验证会话票据有效性；若验证失

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

TLS 1.3 0-RTT (Early Data) 机制允许客户端在重连时发送应用数据与 ClientHello 一起，但服务器需验证会话票据有效性；若验证失败，数据将被丢弃，可能导致重传，因此 0-RTT 仅在服务器配置了 strict validation 且网络可靠时能真正节省 1 RTT 的应用层延迟。

## Corrected Claim

TLS 1.3 0-RTT (Early Data) 机制允许客户端在重连时发送应用数据与 ClientHello 一起，但服务器需验证会话票据有效性；若验证失败，数据将被丢弃，可能导致重传，因此 0-RTT 仅在服务器配置了 strict validation 且网络可靠时能真正节省 1 RTT 的应用层延迟。

## Evidence

先验知识/题面给定，逻辑校验通过
