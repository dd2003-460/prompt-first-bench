# N106: 公有云CDN多AZ冗余下的单点故障影响面为 0% 用户流量（假设 AZ 间流量完全隔离且无共享瓶颈），但跨 AZ 网络抖动可能引入额外延迟 σ_cross_az

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

公有云CDN多AZ冗余下的单点故障影响面为 0% 用户流量（假设 AZ 间流量完全隔离且无共享瓶颈），但跨 AZ 网络抖动可能引入额外延迟 σ_cross_az ≈ 1-3ms，需计入 P99 分布尾部

## Corrected Claim

公有云CDN多AZ冗余下的单点故障影响面为 0% 用户流量（假设 AZ 间流量完全隔离且无共享瓶颈），但跨 AZ 网络抖动可能引入额外延迟 σ_cross_az ≈ 1-3ms，需计入 P99 分布尾部

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交且无冗余，分别定义了量化公式、参数取值范围和参数构成。但存在完备性缺失：父节点明确提到'多AZ冗余下单点故障影响面为0%'这一关键前提/结论，子节点仅聚焦于延迟抖动（Latency），完全未涵盖故障隔离（Availability/Reliability）方面的分解或验证，导致未覆盖父节点的所有关键方面。）

## Search Query

multi-AZ CDN cross-AZ latency jitter impact
