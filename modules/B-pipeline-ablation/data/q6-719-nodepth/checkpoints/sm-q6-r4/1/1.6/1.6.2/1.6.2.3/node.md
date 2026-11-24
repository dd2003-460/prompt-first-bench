# N199: TLS 1.2 会话恢复的命中率取决于客户端重连频率和服务器 Session Ticket 的有效期（通常 7-30 天）；对于高频访问的 C 端用户，假设 8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

TLS 1.2 会话恢复的命中率取决于客户端重连频率和服务器 Session Ticket 的有效期（通常 7-30 天）；对于高频访问的 C 端用户，假设 80% 请求为重连，则平均连接延迟 ≈ 0.2×3RTT + 0.8×2RTT = 2.2 RTT。

## Corrected Claim

TLS 1.2 会话恢复的命中率取决于客户端重连频率和服务器 Session Ticket 的有效期；对于高频访问的 C 端用户，假设 80% 请求为重连，则平均连接延迟 ≈ 0.2×2RTT + 0.8×1RTT = 1.2 RTT（注：TLS 1.2 完整握手通常为 2 RTT，会话恢复通常为 1 RTT）。

## Evidence

[质询]陈述中关于 TLS 1.2 会话恢复的 RTT 计算存在技术错误：TLS 1.2 会话恢复（Session Resumption）通常只需 1 RTT（客户端发送 ClientHello 包含 Session ID/Ticket，服务器回复 ServerHello + Finished），而非 2 RTT；此外，'80% 请求为重连'及'7-30 天有效期'属于特定场景下的经验假设，非通用事实。 | 来源 [2] 指出 Session Resumption 用于优化高频短连接，但未明确 TLS 1.2 恢复握手为 2 RTT；根据 TLS 1.2 标准协议，会话恢复握手通常为 1 RTT，因此 0.8×2RTT 的计算逻辑有误，且经验参数缺乏来源直接支持。

## Search Query

TLS session resumption hit rate mobile client statistics

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/457337593&rut=afcf99a79ff3cc9c6113e03d8118c3e1eee15988b0ce99ad96719b0e3f682228', 'type': 'ddg', 'title': '什么是TLS会话恢复 ( TLS Session Resumption ) - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/1993264287163105297&rut=3877b59c2f498a541d222312477fe438846c9220eb7773d74dfbdab55bcb0cb7', 'type': 'ddg', 'title': 'HTTPS性能损耗有多大？TLS握手过程详解及Session Resumption优化策略'}
