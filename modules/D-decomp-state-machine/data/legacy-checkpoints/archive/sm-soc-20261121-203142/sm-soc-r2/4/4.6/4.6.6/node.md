# N77: 平台价格敏感度绝对值 |∂U_platform/∂P| 的一阶导数表达式为 r * Q + r * P_deal * ∂Q/∂P，需代入 N28 中的 r 及 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

平台价格敏感度绝对值 |∂U_platform/∂P| 的一阶导数表达式为 r * Q + r * P_deal * ∂Q/∂P，需代入 N28 中的 r 及 N12 中的平均溢价 5% 进行数值估算。

## Corrected Claim

平台价格敏感度绝对值 |∂U_platform/∂P| 的一阶导数表达式为 r * Q + r * P_deal * ∂Q/∂P，需代入 N28 中的 r 及 N12 中的平均溢价 5% 进行数值估算。

## Evidence

先验知识/题面给定，逻辑校验通过：根据包络定理或全微分法则，平台效用对价格的一阶导数确实包含直接价格效应项（r*Q）和通过数量变化的间接效应项（r*P_deal*∂Q/∂P），表达式在数学上自洽。
