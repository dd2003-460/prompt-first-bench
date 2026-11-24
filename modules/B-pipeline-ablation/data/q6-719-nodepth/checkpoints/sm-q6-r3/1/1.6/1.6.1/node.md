# N56: Total_Connect_Latency_TLS1.3 = 1 RTT (TCP Handshake) + 1 RTT (TLS 1.3 Handshake)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Total_Connect_Latency_TLS1.3 = 1 RTT (TCP Handshake) + 1 RTT (TLS 1.3 Handshake) = 2 RTT；若启用 0-RTT 恢复会话，则 TLS 协商延迟可降至 0 RTT（仅首次连接为 2 RTT）[待核验]

## Corrected Claim

Total_Connect_Latency_TLS1.3 = 1 RTT (TCP Handshake) + 1 RTT (TLS 1.3 Handshake) = 2 RTT；若启用 0-RTT 恢复会话，则 TLS 协商延迟可降至 0 RTT（仅首次连接为 2 RTT）[待核验]

## Evidence

父节点级核验未通过：非正交（子节点2重复了子节点1中关于TLS 1.3握手占用1 RTT的核心事实，且子节点2中关于TCP Fast Open (TFO)的内容超出了父节点定义的范围（父节点仅讨论TLS 1.3基础延迟及0-RTT，未提及TFO优化），导致子节点间存在信息重叠且引入了父节点未涵盖的额外变量，破坏了正交性。）

## Search Query

TLS 1.3 0-RTT resumption latency reduction
