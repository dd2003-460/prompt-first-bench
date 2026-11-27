# N495: A100 SXM NVLink 通信延迟修正：基于修正后的 256 KB 总通信量 (Batch=1)，NVLink 600 GB/s 下的传输时间为 256 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N168

## Claim

A100 SXM NVLink 通信延迟修正：基于修正后的 256 KB 总通信量 (Batch=1)，NVLink 600 GB/s 下的传输时间为 256 KB / 600 GB/s ≈ 0.0004 ms (0.4 μs)；N168 中 14.3 ms 的估计基于错误的 8.58 GB 数据量，实际延迟可忽略不计。

## Corrected Claim

A100 SXM NVLink 通信延迟修正：基于修正后的 256 KB 总通信量 (Batch=1)，NVLink 600 GB/s 下的传输时间为 256 KB / 600 GB/s ≈ 0.0004 ms (0.4 μs)；N168 中 14.3 ms 的估计基于错误的 8.58 GB 数据量，实际延迟可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：256 KB / 600 GB/s ≈ 0.4 μs 计算正确，且 NVLink 延迟远低于 14.3 ms 符合物理直觉
