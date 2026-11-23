# N338: 流量分布均匀假设下，$B_{95} \approx B_{peak}$的近似成立条件是：流量在24小时内呈正弦或钟形分布，且$K_{peak}$定义清晰为$B_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

流量分布均匀假设下，$B_{95} \approx B_{peak}$的近似成立条件是：流量在24小时内呈正弦或钟形分布，且$K_{peak}$定义清晰为$B_{peak}/B_{avg}$。

## Corrected Claim

流量分布均匀假设下，$B_{95} \approx B_{peak}$的近似成立条件是：流量在24小时内呈正弦或钟形分布，且$K_{peak}$定义清晰为$B_{peak}/B_{avg}$。

## Evidence

先验知识/题面给定，逻辑校验通过：在对称的钟形或正弦分布下，峰值与均值之比（K_peak）通常接近2，而95th百分位流量通常接近峰值流量，因此B_95 ≈ B_peak在特定分布假设下是合理的工程近似。
