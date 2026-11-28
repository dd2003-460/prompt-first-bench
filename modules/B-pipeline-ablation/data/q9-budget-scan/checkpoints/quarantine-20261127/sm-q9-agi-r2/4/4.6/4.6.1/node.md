# N79: Self-Consistency 采样 k=5 次的计算成本需纳入预算：每次采样消耗 27B 模型推理时间约 T_infer，总耗时 5*T_infer；方差计

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Self-Consistency 采样 k=5 次的计算成本需纳入预算：每次采样消耗 27B 模型推理时间约 T_infer，总耗时 5*T_infer；方差计算公式 Var = (1/k)*Σ(x_i - mean)^2，其中 x_i 为第 i 次采样的结论置信度分数（0-1），阈值 0.1 对应标准差 0.316，需确保采样温度 T=0.7 以保证多样性。

## Corrected Claim

Self-Consistency 采样 k=5 次的计算成本需纳入预算：每次采样消耗 27B 模型推理时间约 T_infer，总耗时 5*T_infer；方差计算公式 Var = (1/k)*Σ(x_i - mean)^2，其中 x_i 为第 i 次采样的结论置信度分数（0-1），阈值 0.1 对应标准差 0.316，需确保采样温度 T=0.7 以保证多样性。

## Evidence

先验知识/题面给定，逻辑校验通过：Self-Consistency 成本线性叠加符合直觉；方差公式及阈值与标准差的换算（sqrt(0.1)≈0.316）数学正确；温度设置符合采样多样性常识。

## Search Query

self-consistency sampling temperature variance threshold LLM reasoning
