# N366: 无截断风险的结论仅在单轮推理中成立，在多轮对话或长程任务中，累积上下文长度 L_cumulative = Σ L_t 超过 262k 的概率需通过马尔可夫链模型

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

无截断风险的结论仅在单轮推理中成立，在多轮对话或长程任务中，累积上下文长度 L_cumulative = Σ L_t 超过 262k 的概率需通过马尔可夫链模型计算，其中每轮新增上下文长度的均值 μ_round 和方差 σ²_round 是关键参数

## Corrected Claim

无截断风险的结论仅在单轮推理中成立，在多轮对话或长程任务中，累积上下文长度 L_cumulative = Σ L_t 超过 262k 的概率需通过马尔可夫链模型计算，其中每轮新增上下文长度的均值 μ_round 和方差 σ²_round 是关键参数

## Evidence

先验知识/题面给定，逻辑校验通过：多轮对话上下文累积确实构成随机过程，使用马尔可夫链或随机游走模型估算超过阈值概率是合理的数学建模方法，参数定义符合统计学常识。
