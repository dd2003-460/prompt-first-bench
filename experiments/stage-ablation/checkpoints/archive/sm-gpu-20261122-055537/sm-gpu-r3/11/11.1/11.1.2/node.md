# N375: Qwen3-27B 总层数为 54 层，TP=2 方案下总通信数据量 Total_Comm = 54 * 1.0 MB = 54 MB。在 PCIe 4.0 x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

Qwen3-27B 总层数为 54 层，TP=2 方案下总通信数据量 Total_Comm = 54 * 1.0 MB = 54 MB。在 PCIe 4.0 x16 有效带宽 16-22 GB/s 下，通信耗时 T_comm = Total_Comm / Bandwidth ≈ 54 MB / 20 GB/s ≈ 2.7 ms（取中间值 20 GB/s）。

## Corrected Claim

Qwen3-27B 总层数为 54 层，TP=2 方案下总通信数据量 Total_Comm = 54 * 1.0 MB = 54 MB。在 PCIe 4.0 x16 有效带宽 16-22 GB/s 下，通信耗时 T_comm = Total_Comm / Bandwidth ≈ 54 MB / 20 GB/s ≈ 2.7 ms（取中间值 20 GB/s）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构确为 54 层，TP=2 下每层通信量约 1MB（基于激活值大小估算），总通信量 54MB 与 PCIe 4.0 带宽下的耗时计算在量级和逻辑上均自洽。
