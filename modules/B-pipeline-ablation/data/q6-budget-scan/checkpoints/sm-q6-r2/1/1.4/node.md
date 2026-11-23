# N9: 混合策略技术可行性阈值：自建POP与公有云CDN之间的请求路由切换延迟 Δt_switch 需满足 Δt_switch ≤ ε，其中 ε 为可接受的路由抖动上限

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

混合策略技术可行性阈值：自建POP与公有云CDN之间的请求路由切换延迟 Δt_switch 需满足 Δt_switch ≤ ε，其中 ε 为可接受的路由抖动上限（通常 < 5ms），否则混合策略因路由复杂性导致P99恶化

## Corrected Claim

混合策略技术可行性阈值：自建POP与公有云CDN之间的请求路由切换延迟 Δt_switch 需满足 Δt_switch ≤ ε，其中 ε 为可接受的路由抖动上限（通常 < 5ms），否则混合策略因路由复杂性导致P99恶化

## Evidence

父节点级核验未通过：不完备（子节点在维度上基本正交，分别涵盖了DNS、TLS、控制面逻辑和数据一致性四个不同的延迟来源，不存在明显的重复或矛盾。然而，完备性存在严重缺陷：父节点讨论的是“混合策略”中自建POP与公有云CDN之间的路由切换，这必然涉及跨节点/跨域的网络传输延迟（RTT）以及连接建立/复用的底层网络开销。子节点仅列举了DNS、TLS、API调用和缓存一致性，完全缺失了最核心的“网络传输延迟（Network RTT/Latency）”这一项，且未解释这些子项如何具体加和或竞争构成 Δt_switch。此外，缓存一致性延迟（秒级）通常不属于路由切换的瞬时延迟（毫秒级），将其作为 Δt_switch 的组成部分在逻辑上是不成立的，它影响的是内容新鲜度而非路由切换本身的耗时。）

## Search Query

hybrid CDN self-built edge node routing switch latency overhead
