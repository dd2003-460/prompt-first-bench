# N233: 代码生成任务的可接受性判定公式：Relative_Loss_Code = (Pass@1_base - Pass@1_W4) / Pass@1_base；判定条

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

代码生成任务的可接受性判定公式：Relative_Loss_Code = (Pass@1_base - Pass@1_W4) / Pass@1_base；判定条件为 Relative_Loss_Code <= 0.10；若 Pass@1_base = 0.75 且 Pass@1_W4 = 0.68，则 Relative_Loss_Code ≈ 9.3% < 10%，判定为可接受；需代入实际检索到的 N118 和 N119 数值进行最终判定。

## Corrected Claim

代码生成任务的可接受性判定公式：Relative_Loss_Code = (Pass@1_base - Pass@1_W4) / Pass@1_base；判定条件为 Relative_Loss_Code <= 0.10；若 Pass@1_base = 0.75 且 Pass@1_W4 = 0.68，则 Relative_Loss_Code ≈ 9.3% < 10%，判定为可接受；需代入实际检索到的 N118 和 N119 数值进行最终判定。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值计算 (0.75-0.68)/0.75 ≈ 9.33% 符合数学逻辑，且小于 10% 阈值，判定结论自洽。
