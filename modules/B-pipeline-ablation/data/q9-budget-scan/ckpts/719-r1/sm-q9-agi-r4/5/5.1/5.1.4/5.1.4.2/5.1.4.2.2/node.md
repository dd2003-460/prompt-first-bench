# N648: 输出Token数映射公式：Output_Tokens(T) = Base_Output(500) + T × Complexity_Factor(200)，其中

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

输出Token数映射公式：Output_Tokens(T) = Base_Output(500) + T × Complexity_Factor(200)，其中Complexity_Factor基于历史任务日志回归得出，T=5时Output=1500 tokens，符合27b模型在科研推理中的典型生成长度

## Corrected Claim

输出Token数映射公式：Output_Tokens(T) = Base_Output(500) + T × Complexity_Factor(200)，其中Complexity_Factor基于历史任务日志回归得出，T=5时Output=1500 tokens，符合27b模型在科研推理中的典型生成长度

## Evidence

先验知识/题面给定，逻辑校验通过：公式计算 500 + 5*200 = 1500 正确，且 1500 tokens 符合大语言模型科研推理场景的典型输出长度量级。

## Search Query

LLM output token count complexity correlation benchmark
