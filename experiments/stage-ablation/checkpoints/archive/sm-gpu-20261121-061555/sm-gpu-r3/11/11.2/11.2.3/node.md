# N372: HumanEval Pass@1 下降幅度 Delta_HumanEval = Pass_BF16 - Pass_AWQ_W4A16，需计算具体差值并判断是否落

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131

## Claim

HumanEval Pass@1 下降幅度 Delta_HumanEval = Pass_BF16 - Pass_AWQ_W4A16，需计算具体差值并判断是否落在 1-2% 区间；代码生成任务对量化噪声敏感，若下降 >2% 需标记 [代码能力受损] 并考虑提升至 W8 或 BF16。

## Corrected Claim

HumanEval Pass@1 下降幅度 Delta_HumanEval = Pass_BF16 - Pass_AWQ_W4A16，需计算具体差值并判断是否落在 1-2% 区间；代码生成任务对量化噪声敏感，若下降 >2% 需标记 [代码能力受损] 并考虑提升至 W8 或 BF16。

## Evidence

先验知识/题面给定，逻辑校验通过
