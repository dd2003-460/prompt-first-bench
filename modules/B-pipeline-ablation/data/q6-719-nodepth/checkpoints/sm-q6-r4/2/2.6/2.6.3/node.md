# N86: 混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理分布决定）。

## Corrected Claim

混合策略下长尾区域日均下载流量 (V_tail, GB) 计算为 2000GB * (1 - P_core)，其中 P_core 为核心区域流量占比（由用户地理分布决定）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1定义了输入参数P_core，子节点2基于该参数计算输出V_tail。两者在逻辑上是“输入”与“输出”的关系，而非同一维度的并列分类，因此不冲突（正交）。父节点公式涉及总流量（隐含常数2000GB）、P_core和V_tail，子节点覆盖了核心变量P_core的取值和最终结果V_tail的计算，关键方面覆盖完整。虽然V_tail依赖于P_core，但作为“参数定义”和“结果计算”两个步骤，这是合理的分解，不构成冗余（即不是同一个参数的不同取值，而是一个变量和一个由它导出的结果）。）
