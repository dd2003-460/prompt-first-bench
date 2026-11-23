# N50: 可用性SLA与故障降级策略对成本的影响：自建节点若发生单点故障，需启用备用节点或降级至公有云，故障切换时间 T_failover ∈ [30s, 300s]；公

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

可用性SLA与故障降级策略对成本的影响：自建节点若发生单点故障，需启用备用节点或降级至公有云，故障切换时间 T_failover ∈ [30s, 300s]；公有云CDN的SLA通常为99.9%（年停机<8.76小时），自建需达到同等SLA需增加冗余硬件成本 C_redundancy = C_infra_self * (1/N + 1) * redundancy_factor，其中redundancy_factor通常为1.2-1.5。

## Corrected Claim

自建节点故障切换时间通常在秒级至分钟级（具体取决于架构，如30s-300s为常见经验值）；公有云CDN SLA通常为99.9%（年停机<8.76小时）；自建同等SLA需增加冗余硬件，成本通常为基础基础设施成本的1.2-1.5倍或更高（具体系数取决于冗余策略，如N+1或双活），原公式为特定经验估算模型，非通用物理/经济定律。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别聚焦于故障切换时间（时间维度/性能）、冗余硬件成本（资本/运营支出维度）和故障期间的用户体验/业务损失（机会成本/隐性成本维度），三者维度正交，无重复内容。三者共同构成了父节点中提到的'成本影响'的完整闭环（直接硬件成本+间接业务损失+时间约束），覆盖了父节点的所有关键方面。未发现冗余，每个子节点提供了独立的量化模型或参数定义。）

## Retrieval Sources

- {'url': 'https://codewave.163.com/info/high-availability-sla-design.html&rut=632f3e806284cb47ed9f3c10b199c1c8102c097cb9db2c20f22bea9f05aba7f6', 'type': 'ddg', 'title': '业务系统可用性设计方法：停机预算、冗余分层与故障演练要点-网易Codewave'}
