# N43: 路由决策逻辑开销 t_logic = t_algorithm + t_api_call，其中 t_algorithm 为负载均衡算法计算时间（<1ms），t_a

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

路由决策逻辑开销 t_logic = t_algorithm + t_api_call，其中 t_algorithm 为负载均衡算法计算时间（<1ms），t_api_call 为向控制平面查询路由策略的API调用延迟（典型 5-50ms）；该值反映混合策略中动态路由决策的实时性开销。

## Corrected Claim

路由决策逻辑开销 t_logic = t_algorithm + t_api_call，其中 t_algorithm 为负载均衡算法计算时间（<1ms），t_api_call 为向控制平面查询路由策略的API调用延迟（典型 5-50ms）；该值反映混合策略中动态路由决策的实时性开销。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

load balancer API call latency ms
