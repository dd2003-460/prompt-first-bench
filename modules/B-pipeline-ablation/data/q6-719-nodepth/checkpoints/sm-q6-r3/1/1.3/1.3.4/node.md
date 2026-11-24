# N59: 自建 POP 回源延迟 T_origin_fetch_self 的 P99 值：POP 到源站的链路通常为专线或 BGP 多线，P99(T_origin_fet

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建 POP 回源延迟 T_origin_fetch_self 的 P99 值：POP 到源站的链路通常为专线或 BGP 多线，P99(T_origin_fetch_self) 约为 30-80ms，低于公有云的回源延迟（因路径更短且可控）。

## Corrected Claim

自建 POP 回源延迟 T_origin_fetch_self 的 P99 值：POP 到源站的链路通常为专线或 BGP 多线，P99(T_origin_fetch_self) 约为 30-80ms，低于公有云的回源延迟（因路径更短且可控）。

## Evidence

父节点级核验未通过：有冗余（子节点通过不同的接入链路类型（同城/跨省/跨大区）划分，逻辑上互斥且覆盖了父节点中30-80ms的延迟范围，正交性和完备性良好。然而，三个子节点本质上是同一物理参数（链路距离/类型）在不同取值下的性能与成本表现，属于典型的参数扫描（Parameter Sweep），而非独立的结构性分解维度。）

## Search Query

Self-built POP origin fetch latency P99 30-80ms dedicated line BGP
