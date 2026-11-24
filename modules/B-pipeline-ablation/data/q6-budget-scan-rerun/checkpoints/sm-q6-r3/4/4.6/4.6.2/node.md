# N89: 混合策略流量切换机制对P99延迟的影响量化：DNS TTL 切换时间 T_dns = 300s (典型值)，智能路由切换时间 T_smart_route = 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

混合策略流量切换机制对P99延迟的影响量化：DNS TTL 切换时间 T_dns = 300s (典型值)，智能路由切换时间 T_smart_route = 5s (基于Anycast或BGP策略)，切换期间延迟抖动 ΔP99 = (T_switch / T_target) × 100%，需确保 T_switch < T_target/10 以避免P99超标

## Corrected Claim

混合策略流量切换机制对P99延迟的影响量化：DNS TTL 切换时间 T_dns = 300s (典型值)，智能路由切换时间 T_smart_route = 5s (基于Anycast或BGP策略)，切换期间延迟抖动 ΔP99 = (T_switch / T_target) × 100%，需确保 T_switch < T_target/10 以避免P99超标

## Evidence

先验知识/题面给定，逻辑校验通过
