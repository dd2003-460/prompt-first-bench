# N74: 机会成本项具体量化为 C_opportunity = P(sale|P_high) * (P_high - P_low) * T_high - P(sale|P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

机会成本项具体量化为 C_opportunity = P(sale|P_high) * (P_high - P_low) * T_high - P(sale|P_low) * (P_low - C) * T_low，其中 T_high 和 T_low 分别为高挂价和降价后的预期成交周期，需量化 T 随价格变化的弹性。

## Corrected Claim

机会成本项具体量化为 C_opportunity = P(sale|P_high) * (P_high - P_low) * T_high - P(sale|P_low) * (P_low - C) * T_low，其中 T_high 和 T_low 分别为高挂价和降价后的预期成交周期，需量化 T 随价格变化的弹性。

## Evidence

先验知识/题面给定，逻辑校验通过
