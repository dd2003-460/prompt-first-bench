# N65: 工作点A的边际成本计算公式 C_A = (P_total × T_cycle) / (E_queries_per_cycle × 1000) × Price_k

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点A的边际成本计算公式 C_A = (P_total × T_cycle) / (E_queries_per_cycle × 1000) × Price_kWh，其中 P_total=300W，Price_kWh=$0.1，T_cycle 需实测 27B 模型生成 512 tokens 的平均墙钟时间（秒），E_queries_per_cycle 定义为单位时间内可完成的完整科研查询数，当前假设 50 queries/min 需替换为实测值 T_cycle 倒数乘以批处理效率因子。

## Corrected Claim

工作点A的边际成本计算公式 C_A = (P_total × T_cycle) / (E_queries_per_cycle × 1000) × Price_kWh，其中 P_total=300W，Price_kWh=$0.1，T_cycle 需实测 27B 模型生成 512 tokens 的平均墙钟时间（秒），E_queries_per_cycle 定义为单位时间内可完成的完整科研查询数，当前假设 50 queries/min 需替换为实测值 T_cycle 倒数乘以批处理效率因子。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（功率×时间/能量单位换算×电价=货币），变量定义清晰且符合工程常识。
