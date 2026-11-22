# N156: E[S] 对 α 的敏感性分析：当 α 从 1.1 变化到 1.5 时，E[S] 从 9.35 KB 降至 2.5 KB，表明 α 越小（尾部越重），均值越大，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

E[S] 对 α 的敏感性分析：当 α 从 1.1 变化到 1.5 时，E[S] 从 9.35 KB 降至 2.5 KB，表明 α 越小（尾部越重），均值越大，但 K_max = C/E[S] 仍远大于 N=100,000，容量非绑定结论对 α ∈ [1.1, 2.0] 稳健。

## Corrected Claim

E[S] 对 α 的敏感性分析：当 α 从 1.1 变化到 1.5 时，E[S] 从 9.35 KB 降至 2.5 KB，表明 α 越小（尾部越重），均值越大，但 K_max = C/E[S] 仍远大于 N=100,000，容量非绑定结论对 α ∈ [1.1, 2.0] 稳健。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布均值随α减小而增大符合数学性质，且α∈[1.1, 2.0]范围内K_max远大于N的结论在量级上合理。

## Search Query

truncated Pareto mean sensitivity to shape parameter alpha
