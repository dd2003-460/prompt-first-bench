# N372: Migration_Bandwidth_Overhead 的量化定义：指迁移流量占用的 I/O 带宽比例，假设迁移通道独立则 Overhead=0，若共享主存储

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

Migration_Bandwidth_Overhead 的量化定义：指迁移流量占用的 I/O 带宽比例，假设迁移通道独立则 Overhead=0，若共享主存储通道则 Overhead = Migration_Throughput / Total_Storage_Throughput；假设总吞吐 10GB/s，迁移 5GB/s，则 Overhead=0.5。

## Corrected Claim

Migration_Bandwidth_Overhead 的量化定义：指迁移流量占用的 I/O 带宽比例，假设迁移通道独立则 Overhead=0，若共享主存储通道则 Overhead = Migration_Throughput / Total_Storage_Throughput；假设总吞吐 10GB/s，迁移 5GB/s，则 Overhead=0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：定义清晰，公式推导（5/10=0.5）符合算术逻辑，无内部矛盾。
