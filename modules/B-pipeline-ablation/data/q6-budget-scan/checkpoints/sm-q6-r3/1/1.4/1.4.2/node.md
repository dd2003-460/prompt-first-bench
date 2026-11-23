# N42: TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reuse 为会话复用节省时间（若启用Session Resumption，t_reuse ≈ t_handshake）；在混合策略中，若自建POP与公有云CDN证书不同，每次路由切换可能触发重新握手。

## Corrected Claim

TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reuse 为会话复用节省时间（若启用Session Resumption，t_reuse ≈ t_handshake）；在混合策略中，若自建POP与公有云CDN证书不同，每次路由切换可能触发重新握手。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1分解了基础握手耗时，子节点2定义了复用节省量，子节点3量化了混合策略下的重握手概率，子节点4计算了对P99的最终影响。四者分别对应公式中的不同变量和推导步骤，无重复或矛盾，且完整覆盖了父节点中关于基础耗时、复用机制及混合策略特殊性的所有关键方面。）

## Search Query

TLS handshake latency ms
