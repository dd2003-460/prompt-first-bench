# N104: 约束验证不等式：k_size * max(x_i) < 128GB / 100,000 等价于 (C_total / (N * E[size])) * s_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

约束验证不等式：k_size * max(x_i) < 128GB / 100,000 等价于 (C_total / (N * E[size])) * s_max < 128GB / N，化简得 C_total * s_max / E[size] < 128GB。代入 s_max=10GB, E[size]≈5.2KB (来自 N99)，左边 ≈ C_total * 10GB / 5.2KB ≈ C_total * 2000，若 C_total=128GB，则 128GB * 2000 >> 128GB，不等式不成立，表明单对象最大大小远超平均分配空间，需调整 s_max 或接受大对象单独处理。

## Corrected Claim

约束验证不等式：k_size * max(x_i) < 128GB / 100,000 等价于 (C_total / (N * E[size])) * s_max < 128GB / N，化简得 C_total * s_max / E[size] < 128GB。代入 s_max=10GB, E[size]≈5.2KB (来自 N99)，左边 ≈ C_total * 10GB / 5.2KB ≈ C_total * 2000，若 C_total=128GB，则 128GB * 2000 >> 128GB，不等式不成立，表明单对象最大大小远超平均分配空间，需调整 s_max 或接受大对象单独处理。

## Evidence

先验知识/题面给定，逻辑校验通过：代数化简正确（k_size * max(x_i) < 128GB/N 等价于 C_total * s_max / E[size] < 128GB），数值量级估算合理（10GB/5.2KB ≈ 2000，128GB*2000 >> 128GB），结论符合逻辑。
