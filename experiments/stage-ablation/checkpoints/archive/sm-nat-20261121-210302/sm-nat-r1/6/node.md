# N20: LRU 缓存命中率下界的精确计算需引入 Belady's Anomaly 修正或采用 Stack Distance 分布的积分，具体公式为 H = 1 - ∫[

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 缓存命中率下界的精确计算需引入 Belady's Anomaly 修正或采用 Stack Distance 分布的积分，具体公式为 H = 1 - ∫[0, C] P(stack distance > c) dc，其中 C 为缓存容量（字节）。

## Corrected Claim

LRU 缓存命中率下界的精确计算需引入 Belady's Anomaly 修正或采用 Stack Distance 分布的积分，具体公式为 H = 1 - ∫[0, C] P(stack distance > c) dc，其中 C 为缓存容量（字节）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
