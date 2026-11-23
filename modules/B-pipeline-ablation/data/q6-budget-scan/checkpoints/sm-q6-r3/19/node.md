# N416: TCP握手与TLS握手的RTT开销量化：在RTT=30ms的典型国内链路下，标准TCP+TLS 1.2握手需3个RTT（90ms）；启用TCP Fast Ope

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

TCP握手与TLS握手的RTT开销量化：在RTT=30ms的典型国内链路下，标准TCP+TLS 1.2握手需3个RTT（90ms）；启用TCP Fast Open (TFO) 和 TLS 1.3 可将握手RTT减少至2个（60ms）甚至1个（30ms，若会话复用），从而将P99延迟中的协议开销降低30-60ms。

## Corrected Claim

TCP握手与TLS握手的RTT开销量化：在RTT=30ms的典型国内链路下，标准TCP+TLS 1.2握手需3个RTT（90ms）；启用TCP Fast Open (TFO) 和 TLS 1.3 可将握手RTT减少至2个（60ms）甚至1个（30ms，若会话复用），从而将P99延迟中的协议开销降低30-60ms。

## Evidence

来源[2]明确指出传统TCP+TLS需3个RTT，且TFO+TLS 1.3可优化；来源[1]和[3]确认TLS 1.3支持1-RTT及0-RTT（会话复用）机制，逻辑推导与来源一致。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32822843/article/details/167180730&rut=134d8361190cd4aabdfa297b38c2bc3006f189809a8a2a542aa7ab0ce8898834', 'type': 'ddg', 'title': 'Tls握手rtt全解析：从1.2的2-rtt到1.3的0-rtt优化 - Csdn博客'}
- {'url': 'https://moklgydocs.github.io/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%AD%A6%E7%A7%91/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/03_%E4%BC%A0%E8%BE%93%E5%B1%82/15_TLS%E4%B8%8ETCP%E5%90%8C%E6%97%B6%E6%8F%A1%E6%89%8B.html&rut=c862dbb7307db3d9979fdf6cf67ab2747594eb135e18ce07b4a5fe311c31460b', 'type': 'ddg', 'title': 'TLS与TCP同时握手 | Moklgy 的异星基站'}
- {'url': 'https://quant67.com/post/cryptography/22-tls-protocol/tls-protocol.html&rut=6bb340ca1cf465ae6bbcb21f9e2046aebb6a4031b5348e2ba26f3e6889b19879', 'type': 'ddg', 'title': '【密码学百科】Tls 协议全解析：从握手到 0-rtt | 土法炼钢 · 系统与基础设施'}
