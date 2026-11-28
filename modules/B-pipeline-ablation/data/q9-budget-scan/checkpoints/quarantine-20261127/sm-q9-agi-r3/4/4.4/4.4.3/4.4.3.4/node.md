# N212: 两级流水线的总负载节省率 S_total = 0.30 * W_8B + (1 - W_8B) * 0，其中 W_8B 为分配给 8B 的任务权重；若 W_8B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

两级流水线的总负载节省率 S_total = 0.30 * W_8B + (1 - W_8B) * 0，其中 W_8B 为分配给 8B 的任务权重；若 W_8B=0.5（摘要+语法检查占一半 token 流量），则 S_total=15%，实际节省 27B 15% 推理时间，而非理论最大 30%。

## Corrected Claim

两级流水线的总负载节省率 S_total = 0.30 * W_8B + (1 - W_8B) * 0，其中 W_8B 为分配给 8B 的任务权重；若 W_8B=0.5（摘要+语法检查占一半 token 流量），则 S_total=15%，实际节省 27B 15% 推理时间，而非理论最大 30%。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（0.5*0.30 + 0.5*0 = 0.15），符合线性叠加原理。
