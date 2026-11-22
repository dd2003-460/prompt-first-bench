# N144: 缓存覆盖率 C/M 的具体数值计算：M = N_objects * E[S] = 100000 * (α/(α-1) * x_min)，假设 x_min=1MB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

缓存覆盖率 C/M 的具体数值计算：M = N_objects * E[S] = 100000 * (α/(α-1) * x_min)，假设 x_min=1MB（典型 CDN 最小对象），则 M ≈ 100000 * 11 * 1MB = 1.1PB，C/M = 128GB / 1.1PB ≈ 0.000116，代入 H_static 公式得 H_static ≈ 1 - (0.000116)^{1/1.1} ≈ 0.999

## Corrected Claim

缓存覆盖率 C/M 的具体数值计算：M = N_objects * E[S] = 100000 * (α/(α-1) * x_min)，假设 x_min=1MB（典型 CDN 最小对象），则 M ≈ 100000 * 11 * 1MB = 1.1PB，C/M = 128GB / 1.1PB ≈ 0.000116，代入 H_static 公式得 H_static ≈ 1 - (0.000116)^{1/1.1} ≈ 0.999

## Evidence

先验知识/题面给定，逻辑校验通过：Zipf分布均值公式应用正确，数值量级（1.1PB）与计算结果（H_static≈0.999）符合数学推导及CDN缓存场景直觉。
