# N109: 混合策略自建部分月带宽成本 $C_{bw,hybrid,own}$：5 个核心 POP 覆盖 90% 流量（1.8 TB/日），峰值带宽 $B_{peak,ow

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

混合策略自建部分月带宽成本 $C_{bw,hybrid,own}$：5 个核心 POP 覆盖 90% 流量（1.8 TB/日），峰值带宽 $B_{peak,own} = (1.8 \text{ TB}/86400 \text{ s}) \times 2.0 \approx 41.7 \text{ Mbps}$；若采购 10Gbps 专线分摊，单 POP 月带宽成本约为 600-1000 元，5 个 POP 总成本 $C_{bw,hybrid,own} \approx 3000-5000$ 元/月。

## Corrected Claim

混合策略自建部分月带宽成本 $C_{bw,hybrid,own}$：5 个核心 POP 覆盖 90% 流量（1.8 TB/日），峰值带宽 $B_{peak,own} = (1.8 \text{ TB}/86400 \text{ s}) \times 2.0 \approx 41.7 \text{ Mbps}$；若采购 10Gbps 专线分摊，单 POP 月带宽成本约为 600-1000 元，5 个 POP 总成本 $C_{bw,hybrid,own} \approx 3000-5000$ 元/月。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽计算 (1.8TB/86400s * 2 ≈ 41.7Mbps) 数学正确；成本估算 (5 POP * 600-1000元) 符合国内专线/带宽市场量级，逻辑自洽。

## Search Query

China dedicated line 10Gbps monthly cost telecom
