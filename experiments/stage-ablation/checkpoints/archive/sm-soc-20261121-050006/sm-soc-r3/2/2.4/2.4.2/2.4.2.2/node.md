# N213: 价格敏感度（∂T_close/∂P_ask）的量化：∂T_close/∂P_ask = -0.02 * T_close / P_ask，基于 N7 的负相关关系

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

价格敏感度（∂T_close/∂P_ask）的量化：∂T_close/∂P_ask = -0.02 * T_close / P_ask，基于 N7 的负相关关系（P_ask 增加 1% 时，T_close 变化 -0.2%），该公式将价格变动转化为成交周期的边际变化率。

## Corrected Claim

价格敏感度（∂T_close/∂P_ask）的量化：∂T_close/∂P_ask = -0.02 * T_close / P_ask，基于 N7 的负相关关系（P_ask 增加 1% 时，T_close 变化 -0.2%），该公式将价格变动转化为成交周期的边际变化率。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ∂T/∂P = -0.02 * T/P 等价于弹性为 -0.02，即价格变动 1% 导致 T 变动 -0.2%，与陈述中基于 N7 的负相关关系描述完全一致，量纲与数值逻辑自洽。
