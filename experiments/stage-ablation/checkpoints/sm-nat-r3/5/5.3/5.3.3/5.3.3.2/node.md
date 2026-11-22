# N239: LFU 提升幅度 ΔH 对 x_max 的敏感性：当 x_max 从 1GB 增至 10GB 时，尾部大对象的字节占比增加，LFU 因优先保留高频小对象而可能丢

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

LFU 提升幅度 ΔH 对 x_max 的敏感性：当 x_max 从 1GB 增至 10GB 时，尾部大对象的字节占比增加，LFU 因优先保留高频小对象而可能丢失部分大对象，但 LRU 同样受容量约束影响，两者差异 ΔH 应小于 1%，N84 中声称的 -3% 需通过截断 Pareto 数值积分验证

## Corrected Claim

LFU 提升幅度 ΔH 对 x_max 的敏感性：当 x_max 从 1GB 增至 10GB 时，尾部大对象的字节占比增加，LFU 因优先保留高频小对象而可能丢失部分大对象，但 LRU 同样受容量约束影响，两者差异 ΔH 应小于 1%，N84 中声称的 -3% 需通过截断 Pareto 数值积分验证

## Evidence

先验知识/题面给定，逻辑校验通过
