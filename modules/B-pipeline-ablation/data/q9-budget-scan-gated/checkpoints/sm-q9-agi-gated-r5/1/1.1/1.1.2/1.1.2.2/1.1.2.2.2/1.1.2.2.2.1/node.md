# N154: 修正 N79 中 PCIe 延迟计算：128 KB 在 PCIe 3.0 x16（有效带宽约 12-16 GB/s）下的传输时间为 128 KB / 12 GB

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

修正 N79 中 PCIe 延迟计算：128 KB 在 PCIe 3.0 x16（有效带宽约 12-16 GB/s）下的传输时间为 128 KB / 12 GB/s ≈ 10.7 μs，而非 N79 声称的 7.8 μs。这一修正使得在 PCIe 拓扑下，通信延迟占比从 0.052% 升至约 0.071%，仍远低于 1% 的可感知阈值，不构成瓶颈。

## Corrected Claim

修正 N79 中 PCIe 延迟计算：128 KB 在 PCIe 3.0 x16（有效带宽约 12-16 GB/s）下的传输时间为 128 KB / 12 GB/s ≈ 10.7 μs，而非 N79 声称的 7.8 μs。这一修正使得在 PCIe 拓扑下，通信延迟占比从 0.052% 升至约 0.071%，仍远低于 1% 的可感知阈值，不构成瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：128KB/12GB/s ≈ 10.67μs，计算正确；PCIe 3.0 x16 有效带宽 12-16 GB/s 符合工程常识；延迟占比变化趋势及未构成瓶颈的结论逻辑自洽。
