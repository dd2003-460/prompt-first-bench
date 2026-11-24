# N295: BGP单跳路由传播延迟 $T_{bgp\_prop}$ 典型值为0.5-2秒（受Update消息处理、路径向量计算及邻居通知影响），若启用Graceful Re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

BGP单跳路由传播延迟 $T_{bgp\_prop}$ 典型值为0.5-2秒（受Update消息处理、路径向量计算及邻居通知影响），若启用Graceful Restart或Fast Convergence机制，可缩短至0.1-0.5秒。

## Corrected Claim

BGP单跳路由传播延迟 $T_{bgp\_prop}$ 典型值为0.5-2秒（受Update消息处理、路径向量计算及邻居通知影响），若启用Graceful Restart或Fast Convergence机制，可缩短至0.1-0.5秒。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

BGP route propagation delay per hop seconds
