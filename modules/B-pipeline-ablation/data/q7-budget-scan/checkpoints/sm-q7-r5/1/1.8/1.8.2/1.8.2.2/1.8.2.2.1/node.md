# N438: HDD 冷数据首次访问的 P99 延迟增量 ΔLatency_first_access = T_spinup (0.5-1.0s) + T_seek (平均 5

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

HDD 冷数据首次访问的 P99 延迟增量 ΔLatency_first_access = T_spinup (0.5-1.0s) + T_seek (平均 5-10ms for 16TB CMR) + T_transfer (1KB/150MB/s ≈ 0.007ms)，主导项为 T_spinup，导致首次访问延迟相比热数据增加 >1000x

## Corrected Claim

HDD 冷数据首次访问的 P99 延迟增量 ΔLatency_first_access = T_spinup (0.5-1.0s) + T_seek (平均 5-10ms for 16TB CMR) + T_transfer (1KB/150MB/s ≈ 0.007ms)，主导项为 T_spinup，导致首次访问延迟相比热数据增加 >1000x

## Evidence

先验知识/题面给定，逻辑校验通过：HDD冷启动主要耗时在于电机旋转（Spin-up，通常0.5-2秒），远大于寻道（毫秒级）和传输时间，因此P99延迟增量主要由T_spinup主导，数量级估算合理。
