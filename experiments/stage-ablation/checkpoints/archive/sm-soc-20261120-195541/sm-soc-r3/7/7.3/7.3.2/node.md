# N186: 退货率 R_return 与挂价偏差 (P_ask/P_market - 1) 的线性关系：R_return = R_base + γ1*(P_ask/P_ma

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

退货率 R_return 与挂价偏差 (P_ask/P_market - 1) 的线性关系：R_return = R_base + γ1*(P_ask/P_market - 1)，其中 R_base 为基准退货率（假设 5%），γ1 为价格敏感度系数（假设 0.1），当挂价偏差超过 20% 时，R_return 预计达到 7%，需通过 A/B 测试验证 γ1 的实际值。

## Corrected Claim

退货率 R_return 与挂价偏差 (P_ask/P_market - 1) 的线性关系：R_return = R_base + γ1*(P_ask/P_market - 1)，其中 R_base 为基准退货率（假设 5%），γ1 为价格敏感度系数（假设 0.1），当挂价偏差超过 20% 时，R_return 预计达到 7%，需通过 A/B 测试验证 γ1 的实际值。

## Evidence

先验知识/题面给定，逻辑校验通过
