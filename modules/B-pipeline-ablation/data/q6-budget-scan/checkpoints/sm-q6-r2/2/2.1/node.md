# N11: P99 延迟 $L_{p99}$ 由三段组成：$L_{p99} = L_{edge} + L_{backhaul} + L_{processing}$，其中 $

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

P99 延迟 $L_{p99}$ 由三段组成：$L_{p99} = L_{edge} + L_{backhaul} + L_{processing}$，其中 $L_{edge}$ 为边缘节点处理延迟（通常 <5ms），$L_{backhaul}$ 为回源或跨节点传输延迟（取决于拓扑），$L_{processing}$ 为应用层处理延迟（通常 <10ms）。

## Corrected Claim

P99 延迟 $L_{p99}$ 由三段组成：$L_{p99} = L_{edge} + L_{backhaul} + L_{processing}$，其中 $L_{edge}$ 为边缘节点处理延迟（通常 <5ms），$L_{backhaul}$ 为回源或跨节点传输延迟（取决于拓扑），$L_{processing}$ 为应用层处理延迟（通常 <10ms）。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（父节点讨论的是延迟（Latency）的组成（边缘、回源、处理），而所有子节点讨论的均是带宽（Bandwidth）的计算、计费及预留策略。子节点与父节点主题完全不符（领域错位），导致无法覆盖父节点内容；同时子节点内部存在大量关于 $K_{peak}$、$B_{peak}$ 和带宽策略的重复与交叉，缺乏正交性。）

## Search Query

CDN latency components edge backhaul processing time breakdown
