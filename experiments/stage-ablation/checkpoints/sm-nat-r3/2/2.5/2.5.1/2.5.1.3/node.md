# N164: 若采用更保守的 x_max=100MB，E[S]_truncated ≈ 1.1 * 0.794 * (100^{0.1} - 1) / 0.1 ≈ 1.1 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

若采用更保守的 x_max=100MB，E[S]_truncated ≈ 1.1 * 0.794 * (100^{0.1} - 1) / 0.1 ≈ 1.1 * 0.794 * 0.259 / 0.1 ≈ 22.6KB，则 N_128 = 128GB / 22.6KB ≈ 5,900,000，仍大于 100,000，Byte_Coverage_128 仍为 100%，说明在典型 CDN 参数下容量约束非瓶颈。

## Corrected Claim

若采用更保守的 x_max=100MB，E[S]_truncated ≈ 1.1 * 0.794 * (100^{0.1} - 1) / 0.1 ≈ 1.1 * 0.794 * 0.259 / 0.1 ≈ 22.6KB，则 N_128 = 128GB / 22.6KB ≈ 5,900,000，仍大于 100,000，Byte_Coverage_128 仍为 100%，说明在典型 CDN 参数下容量约束非瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算准确（100^0.1≈1.259，(1.259-1)/0.1≈2.59，1.1*0.794*2.59≈22.6KB；128GB/22.6KB≈5.9M），结论符合逻辑。
