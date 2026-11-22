# N50: 显存容量可行性判据：对于候选卡显存容量 C (GB)，必须满足 C ≥ 54 (权重) + 0.128 × N (KV Cache) + 2 (Activati

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

显存容量可行性判据：对于候选卡显存容量 C (GB)，必须满足 C ≥ 54 (权重) + 0.128 × N (KV Cache) + 2 (Activations) + 2 (Overhead)，其中 N 为并发序列数；该不等式定义了各精度下最小显存阈值。

## Corrected Claim

显存容量可行性判据：对于候选卡显存容量 C (GB)，必须满足 C ≥ 54 (权重) + 0.128 × N (KV Cache) + 2 (Activations) + 2 (Overhead)，其中 N 为并发序列数；该不等式定义了各精度下最小显存阈值。

## Evidence

先验知识/题面给定，逻辑校验通过
