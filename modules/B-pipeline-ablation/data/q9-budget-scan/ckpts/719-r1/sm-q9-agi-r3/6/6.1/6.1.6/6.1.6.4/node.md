# N264: CoT (Chain-of-Thought) 提示在假设生成任务上的成功率提升幅度量化：设零样本成功率为 P_base，CoT 成功率为 P_cot，提升幅度 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

CoT (Chain-of-Thought) 提示在假设生成任务上的成功率提升幅度量化：设零样本成功率为 P_base，CoT 成功率为 P_cot，提升幅度 Delta = (P_cot - P_base) / P_base。基于 GSM8K 类似逻辑推理任务的公开基准，Delta 约为 0.25 (25%)，即若 P_base=0.4，则 P_cot=0.5。

## Corrected Claim

CoT (Chain-of-Thought) 提示在假设生成任务上的成功率提升幅度量化：设零样本成功率为 P_base，CoT 成功率为 P_cot，提升幅度 Delta = (P_cot - P_base) / P_base。基于 GSM8K 类似逻辑推理任务的公开基准，Delta 约为 0.25 (25%)，即若 P_base=0.4，则 P_cot=0.5。

## Evidence

先验知识/题面给定，逻辑校验通过
