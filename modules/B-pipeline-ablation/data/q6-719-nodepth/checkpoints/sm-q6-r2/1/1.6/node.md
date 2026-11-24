# N11: TCP 握手与 TLS 协商延迟：TCP 握手 = 1 RTT，TLS 1.3 协商 = 1 RTT，TLS 1.2 协商 = 2 RTT，总连接建立延迟 = 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

TCP 握手与 TLS 协商延迟：TCP 握手 = 1 RTT，TLS 1.3 协商 = 1 RTT，TLS 1.2 协商 = 2 RTT，总连接建立延迟 = 2-3 RTT [待核验]。

## Corrected Claim

TCP 握手与 TLS 协商延迟：TCP 握手 = 1 RTT，TLS 1.3 协商 = 1 RTT，TLS 1.2 协商 = 2 RTT，总连接建立延迟 = 2-3 RTT [待核验]。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点1和2本质上是同一逻辑（不同TLS版本下的延迟计算）的不同取值，存在冗余；且父节点明确提到“总连接建立延迟 = 2-3 RTT”，但子节点3引入了“Jitter_Factor”和“P99”概念，这超出了父节点定义的“基础握手延迟”范畴，导致完备性错位（父节点未包含统计分布/抖动因素，子节点却引入了新维度）。）

## Search Query

TLS 1.3 handshake RTT count
