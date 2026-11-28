# N238: Cost_Cloud_20% 的成本函数需修正为动态变量：Cost_Cloud(t) = (Input_Tokens(t) × P_in + Output_To

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Cost_Cloud_20% 的成本函数需修正为动态变量：Cost_Cloud(t) = (Input_Tokens(t) × P_in + Output_Tokens(t) × P_out)，其中 Input/Output Tokens 并非固定值，而是任务复杂度 T 的非线性函数，需建立 T 与 Token 消耗的映射曲线以替代 N71 的静态估算

## Corrected Claim

Cost_Cloud_20% 的成本函数需修正为动态变量：Cost_Cloud(t) = (Input_Tokens(t) × P_in + Output_Tokens(t) × P_out)，其中 Input/Output Tokens 并非固定值，而是任务复杂度 T 的非线性函数，需建立 T 与 Token 消耗的映射曲线以替代 N71 的静态估算

## Evidence

先验知识/题面给定，逻辑校验通过：云成本确实由Token数量决定，且Token消耗随任务复杂度非线性增长，修正静态估算符合工程直觉。
