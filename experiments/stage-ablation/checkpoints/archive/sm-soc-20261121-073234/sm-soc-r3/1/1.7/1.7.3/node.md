# N49: 正反馈循环的稳定性边界：迭代函数 P_{t+1} = P_t + α*(P_t - C_t) 收敛的前提是 |1 + α| < 1，即 α < 0；但题面描述为

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

正反馈循环的稳定性边界：迭代函数 P_{t+1} = P_t + α*(P_t - C_t) 收敛的前提是 |1 + α| < 1，即 α < 0；但题面描述为右移（发散），说明实际模型需引入外部约束项（如买家支付意愿上限 W_max），修正为 P_{t+1} = min(P_t + α*(P_t - C_t), W_max)，W_max 的分布决定了右移停止的位置。

## Corrected Claim

正反馈循环的稳定性边界：迭代函数 P_{t+1} = P_t + α*(P_t - C_t) 收敛的前提是 |1 + α| < 1，即 α < 0；但题面描述为右移（发散），说明实际模型需引入外部约束项（如买家支付意愿上限 W_max），修正为 P_{t+1} = min(P_t + α*(P_t - C_t), W_max)，W_max 的分布决定了右移停止的位置。

## Evidence

先验知识/题面给定，逻辑校验通过：迭代函数 P_{t+1} = P_t + α(P_t - C_t) 可重写为 P_{t+1} = (1+α)P_t - αC_t，其收敛条件确实为 |1+α| < 1（即 -2 < α < 0），若 α > 0 则发散，符合正反馈循环特征；引入 min(·, W_max) 约束后，发散过程将在 W_max 处停止，逻辑自洽且符合经济学直觉。

## Search Query

price dynamics positive feedback loop stability condition buyer willingness to pay cap
