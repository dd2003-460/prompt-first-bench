# N369: MMLU 准确率下降幅度 Delta_MMLU = Acc_BF16 - Acc_AWQ_W4A16，需计算具体差值并判断是否落在 0.5-1.5% 区间；若超

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130

## Claim

MMLU 准确率下降幅度 Delta_MMLU = Acc_BF16 - Acc_AWQ_W4A16，需计算具体差值并判断是否落在 0.5-1.5% 区间；若超出该区间，需标记 [质量损失显著] 并重新评估 W4 精度的可行性。

## Corrected Claim

MMLU 准确率下降幅度 Delta_MMLU = Acc_BF16 - Acc_AWQ_W4A16，需计算具体差值并判断是否落在 0.5-1.5% 区间；若超出该区间，需标记 [质量损失显著] 并重新评估 W4 精度的可行性。

## Evidence

先验知识/题面给定，逻辑校验通过
