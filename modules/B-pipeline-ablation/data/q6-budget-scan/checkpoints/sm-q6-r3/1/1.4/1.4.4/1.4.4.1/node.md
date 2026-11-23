# N151: t_invalidate 的传播延迟模型：t_invalidate = t_publish + t_propagate，其中 t_publish 为失效消息发布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

t_invalidate 的传播延迟模型：t_invalidate = t_publish + t_propagate，其中 t_publish 为失效消息发布延迟（<10ms），t_propagate 为多播/组播到所有边缘节点的时间，受限于最慢节点网络 RTT 和消息队列积压；典型值 1-10s 中，1s 以内依赖高效组播（如 IGMP），10s 级别通常因 TCP 逐跳推送或高负载队列导致

## Corrected Claim

t_invalidate 的传播延迟模型：t_invalidate = t_publish + t_propagate，其中 t_publish 为失效消息发布延迟（<10ms），t_propagate 为多播/组播到所有边缘节点的时间，受限于最慢节点网络 RTT 和消息队列积压；典型值 1-10s 中，1s 以内依赖高效组播（如 IGMP），10s 级别通常因 TCP 逐跳推送或高负载队列导致

## Evidence

先验知识/题面给定，逻辑校验通过：失效传播延迟由发布延迟与网络传播延迟（受限于最慢节点RTT及队列积压）组成，符合分布式系统网络通信的基本物理直觉与工程经验，数值量级（毫秒级发布+秒级传播）合理。

## Search Query

CDN cache invalidation propagation delay multicast vs unicast push latency seconds
