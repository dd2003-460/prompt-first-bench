# N279: HDD 层总 IOPS 承载能力修正计算：30 盘 × 180 IOPS/盘 = 5,400 IOPS。对比修正后的需求 1,000 IOPS，HDD 层 IO

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92, N93, N94

## Claim

HDD 层总 IOPS 承载能力修正计算：30 盘 × 180 IOPS/盘 = 5,400 IOPS。对比修正后的需求 1,000 IOPS，HDD 层 IOPS 利用率约为 18.5%，仍满足 IOPS 约束，但需结合吞吐量进一步验证。

## Corrected Claim

HDD 层总 IOPS 承载能力修正计算：30 盘 × 180 IOPS/盘 = 5,400 IOPS。对比修正后的需求 1,000 IOPS，HDD 层 IOPS 利用率约为 18.5%，仍满足 IOPS 约束，但需结合吞吐量进一步验证。

## Evidence

先验知识/题面给定，逻辑校验通过：30*180=5400，1000/5400≈18.5%，计算无误且符合工程常识
