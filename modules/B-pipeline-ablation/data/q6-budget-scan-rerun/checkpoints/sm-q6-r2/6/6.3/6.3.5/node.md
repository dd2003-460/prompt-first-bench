# N163: TCP 拥塞窗口增长对 P99 延迟的影响仅在缓存未命中（Cache Miss）场景下生效，其概率为 (1 - H_strategy)，其中 H_strateg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

TCP 拥塞窗口增长对 P99 延迟的影响仅在缓存未命中（Cache Miss）场景下生效，其概率为 (1 - H_strategy)，其中 H_strategy 为对应策略的缓存命中率；因此，TCP 慢启动对整体 P99 延迟的加权贡献为 T_slow_start * (1 - H_strategy) * P99_traffic_ratio。

## Corrected Claim

TCP 拥塞窗口增长对 P99 延迟的影响仅在缓存未命中（Cache Miss）场景下生效，其概率为 (1 - H_strategy)，其中 H_strategy 为对应策略的缓存命中率；因此，TCP 慢启动对整体 P99 延迟的加权贡献为 T_slow_start * (1 - H_strategy) * P99_traffic_ratio。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP拥塞窗口增长（慢启动）仅在需要建立新连接或重传时显著影响延迟，通常对应缓存未命中场景；加权贡献公式符合概率加权逻辑。
