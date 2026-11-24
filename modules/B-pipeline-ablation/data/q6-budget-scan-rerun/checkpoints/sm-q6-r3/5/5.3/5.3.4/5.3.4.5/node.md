# N281: 回源带宽成本与延迟的权衡：自建POP回源至中心机房使用内部骨干网，带宽成本 $C_{backhaul} = B_{backhaul} \times P_{int

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

回源带宽成本与延迟的权衡：自建POP回源至中心机房使用内部骨干网，带宽成本 $C_{backhaul} = B_{backhaul} \times P_{internal}$，其中 $P_{internal}$ 为内部骨干网带宽单价（¥0.05-0.1/GB，远低于公网¥0.2-0.5/GB）；公有云回源使用公网带宽，成本更高；需量化回源流量占比（10%-15%）对总成本的影响，以及低延迟回源路径（内部骨干网）对P99延迟的改善（减少10-20ms）

## Corrected Claim

回源带宽成本与延迟的权衡：自建POP回源至中心机房使用内部骨干网，带宽成本 $C_{backhaul} = B_{backhaul} \times P_{internal}$，其中 $P_{internal}$ 为内部骨干网带宽单价（¥0.05-0.1/GB，远低于公网¥0.2-0.5/GB）；公有云回源使用公网带宽，成本更高；需量化回源流量占比（10%-15%）对总成本的影响，以及低延迟回源路径（内部骨干网）对P99延迟的改善（减少10-20ms）

## Evidence

先验知识/题面给定，逻辑校验通过：内部骨干网带宽成本显著低于公网符合经济直觉，回源流量占比及延迟改善量级在CDN架构中属于合理工程经验值。
