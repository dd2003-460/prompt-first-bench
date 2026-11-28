# N387: 在 262144 上下文长度下，中间位置 Token 相对于 Query 的平均距离 D_mid 的理论估算值：D_mid ≈ L/3 (L=262144)，即

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

在 262144 上下文长度下，中间位置 Token 相对于 Query 的平均距离 D_mid 的理论估算值：D_mid ≈ L/3 (L=262144)，即 D_mid ≈ 87381；相比开头位置 D_start ≈ L/2 (131072)，距离缩短约 33.3%，用于量化注意力分散的差异基础。

## Corrected Claim

在 262144 上下文长度下，中间位置 Token 相对于 Query 的平均距离 D_mid 的理论估算值：D_mid ≈ L/3 (L=262144)，即 D_mid ≈ 87381；相比开头位置 D_start ≈ L/2 (131072)，距离缩短约 33.3%，用于量化注意力分散的差异基础。

## Evidence

先验知识/题面给定，逻辑校验通过：基于均匀分布假设，中间位置到Query（通常位于末尾或特定位置）的距离估算符合几何平均逻辑，数值计算准确（262144/3 ≈ 87381, 262144/2 = 131072, 差值比例 1/3 ≈ 33.3%）。
