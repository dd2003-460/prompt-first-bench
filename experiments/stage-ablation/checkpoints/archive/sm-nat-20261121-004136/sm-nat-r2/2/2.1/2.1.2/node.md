# N37: 独立假设下 LRU 字节命中率下界 H_LRU_independent 的解析解：H_LRU_independent = 1 - (K_max/N)^(1-β)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

独立假设下 LRU 字节命中率下界 H_LRU_independent 的解析解：H_LRU_independent = 1 - (K_max/N)^(1-β)，代入 K_max≈57600, N=100000, β=0.9，计算得 H_LRU_independent ≈ 1 - (0.576)^0.1 ≈ 0.0556 (即 5.56%)。

## Corrected Claim

独立假设下 LRU 字节命中率下界 H_LRU_independent 的解析解：H_LRU_independent = 1 - (K_max/N)^(1-β)，代入 K_max≈57600, N=100000, β=0.9，计算得 H_LRU_independent ≈ 1 - (0.576)^0.1 ≈ 0.0556 (即 5.56%)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 H = 1 - (K/N)^(1-β) 符合 Zipf 分布下 LRU 命中率的解析推导；数值计算 (0.576)^0.1 ≈ 0.9444，1 - 0.9444 = 0.0556，量级与逻辑均自洽。
