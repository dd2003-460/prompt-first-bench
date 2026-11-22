# N142: ΔH 的上界工作点 2（噪声下限）：考虑 LFU 计数噪声（σ_count/r_i > 10% for r_i < 100），ΔH_min = ΔH_max -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

ΔH 的上界工作点 2（噪声下限）：考虑 LFU 计数噪声（σ_count/r_i > 10% for r_i < 100），ΔH_min = ΔH_max - ΔH_noise，其中 ΔH_noise 为因误驱逐高频对象导致的命中率损失，估算值约为 0.5-1.0 个百分点。

## Corrected Claim

ΔH 的上界工作点 2（噪声下限）：考虑 LFU 计数噪声（σ_count/r_i > 10% for r_i < 100），ΔH_min = ΔH_max - ΔH_noise，其中 ΔH_noise 为因误驱逐高频对象导致的命中率损失，估算值约为 0.5-1.0 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU counter noise impact hit rate
