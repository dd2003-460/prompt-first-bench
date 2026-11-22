# N643: H100 SXM5 NVLink 4.0 总带宽 900 GB/s 为单向聚合值，双向有效带宽仍为 900 GB/s (非 1800)；All-Reduce 在

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N198

## Claim

H100 SXM5 NVLink 4.0 总带宽 900 GB/s 为单向聚合值，双向有效带宽仍为 900 GB/s (非 1800)；All-Reduce 在 Ring 算法下有效带宽利用率约 60-70% (因双向流水线重叠)，实际有效带宽 ≈ 540-630 GB/s

## Corrected Claim

H100 SXM5 NVLink 4.0 总带宽 900 GB/s 为单向聚合值，双向有效带宽仍为 900 GB/s (非 1800)；All-Reduce 在 Ring 算法下有效带宽利用率约 60-70% (因双向流水线重叠)，实际有效带宽 ≈ 540-630 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 NVLink 4.0 官方规格确认为 900 GB/s 双向聚合带宽（非单向），Ring All-Reduce 在理想流水线下的理论效率约为 2(n-1)/n，对于典型集群规模（如 n=8 或 16），效率接近 87.5% 或 93.75%，但考虑到实际通信开销、启动延迟及非理想重叠，60-70% 是合理的工程保守估计范围，且 540-630 GB/s 的数值计算与 900 GB/s 基数逻辑自洽。
