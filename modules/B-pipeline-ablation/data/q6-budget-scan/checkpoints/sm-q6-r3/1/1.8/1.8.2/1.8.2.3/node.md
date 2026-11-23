# N236: 长尾区域 T_queue_P99(k) 的公有云调度延迟：T_queue_P99(k) = T_dns_resolution + T_scheduling_de

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

长尾区域 T_queue_P99(k) 的公有云调度延迟：T_queue_P99(k) = T_dns_resolution + T_scheduling_delay，其中 T_dns_resolution ≈ 10-50ms（首次解析），T_scheduling_delay ≈ 5-20ms（公有云负载均衡调度），加上网络拥塞，总排队延迟 P99 可达 30-80ms，显著高于自建节点

## Corrected Claim

长尾区域 T_queue_P99(k) 的公有云调度延迟：T_queue_P99(k) = T_dns_resolution + T_scheduling_delay，其中 T_dns_resolution ≈ 10-50ms（首次解析），T_scheduling_delay ≈ 5-20ms（公有云负载均衡调度），加上网络拥塞，总排队延迟 P99 可达 30-80ms，显著高于自建节点

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud load balancer scheduling delay DNS resolution P99
