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

父节点级核验未通过：不完备（子节点之间逻辑正交（分别定义公式、参数取值、参数构成），无重复或矛盾。但完备性不足：父节点明确指出“单点故障影响面为 0%”这一关键结论（基于AZ隔离假设），而三个子节点仅聚焦于延迟抖动（P99）的量化，完全缺失了对“故障影响面为0%”这一核心论断的解释、前提条件（如流量完全隔离、无共享瓶颈）的验证或边界条件说明。）

## Search Query

multi-AZ CDN cross-AZ latency jitter impact
