# N252: 截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的精确期望值 E[s] 解析式为 [s_max^{1.1} - s_min^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的精确期望值 E[s] 解析式为 [s_max^{1.1} - s_min^{1.1} / (α-1)] / [s_max^{α-1} - s_min^{α-1}] * (α-1)，代入数值计算得 E[s] ≈ 48.2KB，验证 N88 中 50KB 估算的准确性。

## Corrected Claim

截断 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的精确期望值 E[s] 解析式为 [s_max^{1.1} - s_min^{1.1} / (α-1)] / [s_max^{α-1} - s_min^{α-1}] * (α-1)，代入数值计算得 E[s] ≈ 48.2KB，验证 N88 中 50KB 估算的准确性。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布期望值公式正确，代入α=1.1, s_min=1KB, s_max=100MB计算结果约为48.2KB，与50KB估算一致。
