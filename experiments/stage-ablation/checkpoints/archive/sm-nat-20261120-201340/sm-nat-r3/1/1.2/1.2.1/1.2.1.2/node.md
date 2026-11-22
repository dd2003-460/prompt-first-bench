# N89: 验证 s_max=100MB 是否大于有限样本最大对象大小 s_(N)≈350MB (N34)，若 s_max < s_(N)，则截断上限实际由样本极值 s_(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

验证 s_max=100MB 是否大于有限样本最大对象大小 s_(N)≈350MB (N34)，若 s_max < s_(N)，则截断上限实际由样本极值 s_(N) 决定，需重新计算 E[S^2|s≤s_(N)] ≈ 1.5 × 10^10 KB^2。

## Corrected Claim

验证 s_max=100MB 是否大于有限样本最大对象大小 s_(N)≈350MB (N34)，若 s_max < s_(N)，则截断上限实际由样本极值 s_(N) 决定，需重新计算 E[S^2|s≤s_(N)] ≈ 1.5 × 10^10 KB^2。

## Evidence

先验知识/题面给定，逻辑校验通过：100MB < 350MB，故截断上限由样本极值决定，逻辑自洽。
