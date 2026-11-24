# N173: 双峰混合分布下的加权平均对象大小 s_avg 计算：s_avg = 0.8 × E[s_img] + 0.2 × E[s_vid] = 0.8 × 2MB + 

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

双峰混合分布下的加权平均对象大小 s_avg 计算：s_avg = 0.8 × E[s_img] + 0.2 × E[s_vid] = 0.8 × 2MB + 0.2 × 10MB = 3.6MB，若按中位数计算则 s_median ≈ 3.2MB，用于校准 N50 的分母

## Corrected Claim

双峰混合分布下的加权平均对象大小 s_avg 计算：s_avg = 0.8 × E[s_img] + 0.2 × E[s_vid] = 0.8 × 2MB + 0.2 × 10MB = 3.6MB，若按中位数计算则 s_median ≈ 3.2MB，用于校准 N50 的分母

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.8*2 + 0.2*10 = 3.6 正确；中位数估算 3.2MB 在双峰分布（80%在2MB，20%在10MB）下合理（中位数位于主要峰附近，略高于2MB符合直觉）；量纲一致，无逻辑矛盾。
