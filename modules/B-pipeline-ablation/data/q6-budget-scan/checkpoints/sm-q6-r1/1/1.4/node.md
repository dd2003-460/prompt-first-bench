# N9: 混合策略技术可行性阈值：自建POP与公有云CDN之间的请求路由切换延迟 Δt_switch 需满足 Δt_switch ≤ ε，其中 ε 为可接受的路由抖动上限

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：混合CDN架构中，路由切换延迟若超过毫秒级（如5ms），确实会显著增加长尾延迟（P99），导致混合策略优势丧失，该阈值符合网络工程常识。

## Search Query

hybrid CDN self-built edge node routing switch latency overhead
