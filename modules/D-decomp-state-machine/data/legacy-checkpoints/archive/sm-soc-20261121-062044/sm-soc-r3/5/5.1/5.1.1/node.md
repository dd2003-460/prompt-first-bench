# N237: 逆向筛选假设中 r=0.5 对应的最小显著样本量 n_min_r：由 t = r√(n-2)/√(1-r²) > 1.96 解得 n > 2 + (1.96² 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

逆向筛选假设中 r=0.5 对应的最小显著样本量 n_min_r：由 t = r√(n-2)/√(1-r²) > 1.96 解得 n > 2 + (1.96² * (1-r²)/r²)，代入 r=0.5 得 n > 2 + (3.8416 * 0.75/0.25) = 17.52，即 n_min_r = 18；若 n < 18，即使 r=0.5 也不显著。

## Corrected Claim

逆向筛选假设中 r=0.5 对应的最小显著样本量 n_min_r：由 t = r√(n-2)/√(1-r²) > 1.96 解得 n > 2 + (1.96² * (1-r²)/r²)，代入 r=0.5 得 n > 2 + (3.8416 * 0.75/0.25) = 17.52，即 n_min_r = 18；若 n < 18，即使 r=0.5 也不显著。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

minimum sample size for correlation significance r=0.5 alpha 0.05
