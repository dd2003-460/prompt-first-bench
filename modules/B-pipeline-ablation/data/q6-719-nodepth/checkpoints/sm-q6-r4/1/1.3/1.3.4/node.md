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

父节点级核验未通过：不完备, 有冗余（子节点在逻辑上是同构的（均为“接入方式+延迟+成本”的组合），存在严重冗余；且父节点提到的“路径更短且可控”这一关键定性优势未在子节点中体现，仅罗列了数值区间，缺乏对“可控性”或“稳定性”维度的覆盖，导致不完备。）

## Search Query

Self-built POP origin fetch latency P99 30-80ms dedicated line BGP
