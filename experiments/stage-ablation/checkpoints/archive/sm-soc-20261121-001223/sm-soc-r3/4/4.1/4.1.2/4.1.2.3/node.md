# N164: 损失厌恶对成交周期 T_deal 的非线性影响：当 P_ask > V_reserve 时，卖家拒绝概率 P_reject 急剧上升，导致 T_deal 延长；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

损失厌恶对成交周期 T_deal 的非线性影响：当 P_ask > V_reserve 时，卖家拒绝概率 P_reject 急剧上升，导致 T_deal 延长；需建立 P_reject = 1 / (1 + e^(-k*(P_ask - V_reserve))) 模型，量化 k 值以预测不同溢价率下的平均成交延迟。

## Corrected Claim

损失厌恶对成交周期 T_deal 的非线性影响：当 P_ask > V_reserve 时，卖家拒绝概率 P_reject 急剧上升，导致 T_deal 延长；需建立 P_reject = 1 / (1 + e^(-k*(P_ask - V_reserve))) 模型，量化 k 值以预测不同溢价率下的平均成交延迟。

## Evidence

先验知识/题面给定，逻辑校验通过
