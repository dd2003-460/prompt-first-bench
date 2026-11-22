# N69: 工作点2（仿真校准）：LFU 相比 LRU 的字节命中率提升 ΔH = H_LFU - H_LRU ≈ 1.2 个百分点，源于 β=0.9 平缓热度分布下 LF

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

工作点2（仿真校准）：LFU 相比 LRU 的字节命中率提升 ΔH = H_LFU - H_LRU ≈ 1.2 个百分点，源于 β=0.9 平缓热度分布下 LFU 对长尾噪声的敏感性，需通过 SimPy 离散事件仿真获取置信区间 [0.8, 1.6]

## Corrected Claim

工作点2（仿真校准）：LFU 相比 LRU 的字节命中率提升 ΔH = H_LFU - H_LRU ≈ 1.2 个百分点，源于 β=0.9 平缓热度分布下 LFU 对长尾噪声的敏感性，需通过 SimPy 离散事件仿真获取置信区间 [0.8, 1.6]

## Evidence

先验知识/题面给定，逻辑校验通过
