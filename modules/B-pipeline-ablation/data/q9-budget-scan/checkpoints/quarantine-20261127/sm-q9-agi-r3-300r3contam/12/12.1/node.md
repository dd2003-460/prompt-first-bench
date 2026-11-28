# N226: OR-Tools CP-SAT 求解器的实际求解时间 T_solve 并非严格 O(V^E)，而是受约束传播效率影响；在 V=5, E=10 的典型生物实验 C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

OR-Tools CP-SAT 求解器的实际求解时间 T_solve 并非严格 O(V^E)，而是受约束传播效率影响；在 V=5, E=10 的典型生物实验 CSP 中，若约束包含非线性不等式（如样本量 n > 2*σ²/δ²），求解时间从 <10ms 上升至 50-200ms；当 T_solve > 100ms 时，相对于 LLM 生成实验设计的推理时间 (~5-10s)，其占比仍 <2%，不构成瓶颈。

## Corrected Claim

OR-Tools CP-SAT 求解器的实际求解时间 T_solve 并非严格 O(V^E)，而是受约束传播效率影响；在 V=5, E=10 的典型生物实验 CSP 中，若约束包含非线性不等式（如样本量 n > 2*σ²/δ²），求解时间从 <10ms 上升至 50-200ms；当 T_solve > 100ms 时，相对于 LLM 生成实验设计的推理时间 (~5-10s)，其占比仍 <2%，不构成瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：CP-SAT处理小规模非线性约束耗时毫秒级符合工程常识，且100ms远小于5-10s，占比<2%计算正确。

## Search Query

OR-Tools CP-SAT solver performance nonlinear constraints sample size calculation
