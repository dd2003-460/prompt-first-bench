# N579: 若数据存在缺失值，假设缺失率为 m=10%，且缺失机制为 MAR（随机缺失），则有效样本量需调整为 n_effective = n_observed / (1-

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N206

## Claim

若数据存在缺失值，假设缺失率为 m=10%，且缺失机制为 MAR（随机缺失），则有效样本量需调整为 n_effective = n_observed / (1-m)；为满足 Power=0.8，需采集原始样本 n_raw = 196 / 0.9 ≈ 218，以补偿缺失导致的统计效力损失

## Corrected Claim

若数据存在缺失值，假设缺失率为 m=10%，且缺失机制为 MAR（随机缺失），则有效样本量需调整为 n_effective = n_observed / (1-m)；为满足 Power=0.8，需采集原始样本 n_raw = 196 / 0.9 ≈ 218，以补偿缺失导致的统计效力损失

## Evidence

先验知识/题面给定，逻辑校验通过：在MAR机制下，有效样本量 n_eff = n_raw * (1-m)，故 n_raw = n_required / (1-m)。计算 196 / 0.9 ≈ 217.78，取整为 218，符合统计学基本原理。
