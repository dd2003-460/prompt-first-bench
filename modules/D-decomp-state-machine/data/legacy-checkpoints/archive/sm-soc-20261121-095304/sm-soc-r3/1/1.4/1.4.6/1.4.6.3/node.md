# N117: 为避免触发 N37 中的 N_change > 2 限制，卖家单次降价幅度 ΔP_single 的安全上限为 14%（即 15% 阈值减去 1% 的安全边际），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N40, N41

## Claim

为避免触发 N37 中的 N_change > 2 限制，卖家单次降价幅度 ΔP_single 的安全上限为 14%（即 15% 阈值减去 1% 的安全边际），以避免因四舍五入误差被误判为超限。

## Corrected Claim

为避免触发 N37 中的 N_change > 2 限制，卖家单次降价幅度 ΔP_single 的安全上限为 14%（即 15% 阈值减去 1% 的安全边际），以避免因四舍五入误差被误判为超限。

## Evidence

先验知识/题面给定，逻辑校验通过：15%阈值减去1%安全边际等于14%，符合避免四舍五入误差的逻辑推导。
