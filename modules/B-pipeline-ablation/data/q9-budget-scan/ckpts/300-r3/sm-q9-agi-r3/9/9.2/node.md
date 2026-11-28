# N123: API_Cost 的边际成本函数：API_Cost = (Input_Tokens * Price_In + Output_Tokens * Price_Out

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

API_Cost 的边际成本函数：API_Cost = (Input_Tokens * Price_In + Output_Tokens * Price_Out)，其中 Price_In/Out 随供应商和模型规模变化；对于 ~30B 模型，假设 Price_In=$0.5/M, Price_Out=$1.5/M，单次 5k token 循环成本约为 $0.0025，与本地电费 $0.0005/循环相比，API 成本高 5 倍。

## Corrected Claim

API_Cost 的边际成本函数：API_Cost = (Input_Tokens * Price_In + Output_Tokens * Price_Out)，其中 Price_In/Out 随供应商和模型规模变化；对于 ~30B 模型，假设 Price_In=$0.5/M, Price_Out=$1.5/M，单次 5k token 循环成本约为 $0.0025，与本地电费 $0.0005/循环相比，API 成本高 5 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5000 tokens * $0.5/M = $0.0025），倍数关系正确（$0.0025 / $0.0005 = 5），符合API计费常识。
