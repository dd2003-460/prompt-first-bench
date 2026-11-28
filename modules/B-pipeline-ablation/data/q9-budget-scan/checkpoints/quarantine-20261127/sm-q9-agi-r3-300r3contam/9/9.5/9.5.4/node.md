# N253: 吞吐量拐点的精确求解公式：最大性价比点 L_opt 满足 d(T_throughput(L) * Quality(L))/dL = 0，其中 T_through

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

吞吐量拐点的精确求解公式：最大性价比点 L_opt 满足 d(T_throughput(L) * Quality(L))/dL = 0，其中 T_throughput(L) = T_nominal(L) / (1 + f_oom(L) * T_oom / T_step(L))，Quality(L) 为长上下文下的准确率衰减因子（通常随 L 增加而下降），需联合优化两者。

## Corrected Claim

吞吐量拐点的精确求解公式：最大性价比点 L_opt 满足 d(T_throughput(L) * Quality(L))/dL = 0，其中 T_throughput(L) = T_nominal(L) / (1 + f_oom(L) * T_oom / T_step(L))，Quality(L) 为长上下文下的准确率衰减因子（通常随 L 增加而下降），需联合优化两者。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于微积分求极值的基本原理（导数为零），且吞吐量与质量因子的定义符合系统性能优化的常规建模逻辑，量纲与因果关系自洽。

## Search Query

throughput quality tradeoff long context llm inference optimization
