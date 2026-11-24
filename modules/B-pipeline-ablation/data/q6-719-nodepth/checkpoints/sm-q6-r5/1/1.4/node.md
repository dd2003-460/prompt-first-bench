# N10: 时间波动系数 W(t) = Peak_Load / Avg_Load，典型 C 端平台峰值/均值比为 3-5 倍，决定资源冗余系数及 P99 延迟在高峰期的放大

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

时间波动系数 W(t) = Peak_Load / Avg_Load，典型 C 端平台峰值/均值比为 3-5 倍，决定资源冗余系数及 P99 延迟在高峰期的放大效应。

## Corrected Claim

时间波动系数 W(t) = Peak_Load / Avg_Load，典型 C 端平台峰值/均值比为 3-5 倍，决定资源冗余系数及 P99 延迟在高峰期的放大效应。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了时间维度（峰值持续时间）、性能维度（延迟放大）和成本/资源维度（冗余系数），三者逻辑独立且互不重叠，共同构成了对 W(t) 业务影响的完整解释。）
