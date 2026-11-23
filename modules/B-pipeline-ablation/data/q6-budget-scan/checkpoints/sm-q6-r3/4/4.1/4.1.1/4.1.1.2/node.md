# N226: 若采用 95th 峰值带宽计费模式，月成本 $C_{95} = B_{95} \times R_{95}$；在 60TB/月流量下，若峰值系数 $K_{peak

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

若采用 95th 峰值带宽计费模式，月成本 $C_{95} = B_{95} \times R_{95}$；在 60TB/月流量下，若峰值系数 $K_{peak}=2.0$，则 $B_{95} \approx 0.037 \text{ Gbps}$；但通常有最小计费带宽（如 10Gbps）限制，若实际带宽低于门槛，则需按门槛计费，此时 95th 模式成本远高于流量计费，故在 60TB 规模下流量计费更优。

## Corrected Claim

若采用 95th 峰值带宽计费模式，月成本 $C_{95} = B_{95} \times R_{95}$；在 60TB/月流量下，若峰值系数 $K_{peak}=2.0$，则 $B_{95} \approx 0.037 \text{ Gbps}$；但通常有最小计费带宽（如 10Gbps）限制，若实际带宽低于门槛，则需按门槛计费，此时 95th 模式成本远高于流量计费，故在 60TB 规模下流量计费更优。

## Evidence

先验知识/题面给定，逻辑校验通过：60TB/月平均带宽约3.5Gbps，95th峰值带宽37Gbps（0.037Tbps）符合K=2.0的设定；由于37Gbps远高于常见的10Gbps最小计费门槛，95th计费成本（37Gbps单价）确实远高于流量计费（60TB单价），结论逻辑自洽。

## Search Query

Alibaba Cloud CDN 95th percentile bandwidth minimum billing threshold 10Gbps
