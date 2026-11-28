# N665: 任务复杂度评分函数 Complexity_Score 的归一化定义：CS = α*(Reasoning_Depth/Max_RD) + β*(Context_L

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N243

## Claim

任务复杂度评分函数 Complexity_Score 的归一化定义：CS = α*(Reasoning_Depth/Max_RD) + β*(Context_Length/Max_CL) + γ*(Tool_Use_Freq/Max_TUF)，其中 α=0.4, β=0.3, γ=0.3，各分项归一化至 [0,1]

## Corrected Claim

任务复杂度评分函数 Complexity_Score 的归一化定义：CS = α*(Reasoning_Depth/Max_RD) + β*(Context_Length/Max_CL) + γ*(Tool_Use_Freq/Max_TUF)，其中 α=0.4, β=0.3, γ=0.3，各分项归一化至 [0,1]

## Evidence

先验知识/题面给定，逻辑校验通过
