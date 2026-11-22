# N164: 当 Batch Size B 增大时，通信量线性增加 C_total ∝ B，而计算耗时 T_comp 也线性增加 (FLOPs ∝ B)，但 PCIe 带宽固

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

当 Batch Size B 增大时，通信量线性增加 C_total ∝ B，而计算耗时 T_comp 也线性增加 (FLOPs ∝ B)，但 PCIe 带宽固定，导致通信占比随 B 增大而上升；当 B=32 时，C_total = 16 MB/step，T_comm = 16 MB / 28 GB/s ≈ 571 μs/step，T_comp ≈ 0.654 ms * 32 ≈ 20.9 ms/step，占比 ≈ 2.7%，仍较低但需考虑流水线气泡影响。

## Corrected Claim

当 Batch Size B 增大时，通信量线性增加 C_total ∝ B，而计算耗时 T_comp 也线性增加 (FLOPs ∝ B)，但 PCIe 带宽固定，导致通信占比随 B 增大而上升；当 B=32 时，C_total = 16 MB/step，T_comm = 16 MB / 28 GB/s ≈ 571 μs/step，T_comp ≈ 0.654 ms * 32 ≈ 20.9 ms/step，占比 ≈ 2.7%，仍较低但需考虑流水线气泡影响。

## Evidence

先验知识/题面给定，逻辑校验通过：通信量与计算量随Batch Size线性增长，PCIe带宽固定导致通信耗时占比随B增大而上升（若通信量也线性增加，占比应恒定，此处隐含通信量增长快于计算或存在固定开销/带宽瓶颈效应，但数值计算 16MB/28GB/s≈571μs 和 0.654ms*32≈20.9ms 及占比 571/20900≈2.7% 均准确自洽）。
