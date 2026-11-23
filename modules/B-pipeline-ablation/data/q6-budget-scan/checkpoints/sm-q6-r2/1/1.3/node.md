# N8: 公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = (2TB/8) / 86400 * 峰值系数 k_peak，k_peak通常取3-5

## Corrected Claim

公有云CDN带宽峰值支持能力：公有云CDN单区域带宽峰值上限 B_cloud_max 需满足 B_cloud_max ≥ B_peak，其中 B_peak = (2TB/8) / 86400 * 峰值系数 k_peak，k_peak通常取3-5

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1负责核心约束条件的量化验证（证明带宽非瓶颈），子节点2分析计费模式对成本结构的影响，子节点3提供具体的边际成本参数以支持混合策略计算。三者分别对应‘可行性验证’、‘成本模型选择’和‘具体参数输入’，无重叠或矛盾，且共同覆盖了父节点关于带宽峰值能力及其在系统设计中角色的关键方面。）

## Search Query

Alibaba Cloud CDN bandwidth limit per region peak traffic
