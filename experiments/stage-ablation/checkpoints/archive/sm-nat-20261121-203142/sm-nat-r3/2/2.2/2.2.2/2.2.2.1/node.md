# N105: 当 x_min=1KB 且 C=128GB 时，P(S > C) = (128*1024*1024/1024)^(-1.1) = (131072)^(-1.1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

当 x_min=1KB 且 C=128GB 时，P(S > C) = (128*1024*1024/1024)^(-1.1) = (131072)^(-1.1) ≈ 1.4e-6

## Corrected Claim

当 x_min=1KB 且 C=128GB 时，P(S > C) = (128*1024*1024/1024)^(-1.1) = (131072)^(-1.1) ≈ 1.4e-6

## Evidence

先验知识/题面给定，逻辑校验通过：128GB转换为KB为131072，计算131072的-1.1次方约为1.4e-6，数值量级与数学推导一致。
