# N196: 单次云端推理的综合成本公式 Cost_cloud = (In_Tokens * P_in + Out_Tokens * P_out) / 1,000,000；以

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

单次云端推理的综合成本公式 Cost_cloud = (In_Tokens * P_in + Out_Tokens * P_out) / 1,000,000；以 GPT-4o 为例，若 In=500, Out=1000，则 Cost = (500*2.5 + 1000*10)/1e6 = $0.01125。

## Corrected Claim

单次云端推理的综合成本公式 Cost_cloud = (In_Tokens * P_in + Out_Tokens * P_out) / 1,000,000；以 GPT-4o 为例，若 In=500, Out=1000，则 Cost = (500*2.5 + 1000*10)/1e6 = $0.01125。

## Evidence

先验知识/题面给定，逻辑校验通过：GPT-4o 标准定价为输入 $2.5/M tokens，输出 $10/M tokens，计算公式及数值代入正确（(500*2.5 + 1000*10)/1,000,000 = 0.01125）。
