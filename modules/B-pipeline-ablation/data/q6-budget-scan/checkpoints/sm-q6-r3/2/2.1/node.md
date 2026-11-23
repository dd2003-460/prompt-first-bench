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

父节点级核验未通过：非正交, 不完备, 有冗余（子节点与父节点主题完全错位（父节点讲延迟组成，子节点讲带宽计算与计费）；子节点内部存在严重冗余（节点1、2、3均围绕K_peak和峰值带宽计算展开，且节点2和3逻辑重叠）；未覆盖父节点中L_edge、L_backhaul、L_processing的具体定义或影响因素。）

## Search Query

CDN latency components edge backhaul processing time breakdown
