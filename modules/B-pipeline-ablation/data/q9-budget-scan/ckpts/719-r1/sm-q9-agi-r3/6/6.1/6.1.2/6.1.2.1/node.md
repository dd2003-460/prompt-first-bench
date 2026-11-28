# N251: 长上下文准确率衰减拟合函数：Acc(L) = Acc_base - k * log(L/L_0)，其中 Acc_base=Acc_32k, L_0=32k, k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

长上下文准确率衰减拟合函数：Acc(L) = Acc_base - k * log(L/L_0)，其中 Acc_base=Acc_32k, L_0=32k, k 为衰减系数；需在 L={64k, 128k, 262k} 三点测量 Acc，通过最小二乘法拟合 k 值；若 k > 0.05，则表明存在显著的 lost-in-the-middle 效应，需引入滑动窗口注意力或分段摘要预处理

## Corrected Claim

长上下文准确率衰减拟合函数：Acc(L) = Acc_base - k * log(L/L_0)，其中 Acc_base=Acc_32k, L_0=32k, k 为衰减系数；需在 L={64k, 128k, 262k} 三点测量 Acc，通过最小二乘法拟合 k 值；若 k > 0.05，则表明存在显著的 lost-in-the-middle 效应，需引入滑动窗口注意力或分段摘要预处理

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

long context accuracy decay curve fitting log-linear model LLM benchmark 64k 128k 262k
