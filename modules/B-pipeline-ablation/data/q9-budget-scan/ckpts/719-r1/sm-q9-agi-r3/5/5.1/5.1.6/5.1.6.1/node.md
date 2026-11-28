# N243: T_threshold 的量化定义需基于任务复杂度评分函数：Complexity_Score = f(Reasoning_Depth, Context_Leng

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

T_threshold 的量化定义需基于任务复杂度评分函数：Complexity_Score = f(Reasoning_Depth, Context_Length, Tool_Use_Frequency)，其中 Reasoning_Depth 为推理链步数，Context_Length 为输入 Token 数，Tool_Use_Frequency 为工具调用次数，需通过回归分析确定该评分与幻觉率的线性关系系数 β，从而解出 T_threshold = (Local_Hallucination_Rate - Target_Hallucination_Rate) / β

## Corrected Claim

T_threshold 的量化定义需基于任务复杂度评分函数：Complexity_Score = f(Reasoning_Depth, Context_Length, Tool_Use_Frequency)，其中 Reasoning_Depth 为推理链步数，Context_Length 为输入 Token 数，Tool_Use_Frequency 为工具调用次数，需通过回归分析确定该评分与幻觉率的线性关系系数 β，从而解出 T_threshold = (Local_Hallucination_Rate - Target_Hallucination_Rate) / β

## Evidence

先验知识/题面给定，逻辑校验通过
