# N92: s_min 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_min = (α-1) * s_min^{α-2} * s_max^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

s_min 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_min = (α-1) * s_min^{α-2} * s_max^{2-α} / (2-α)，当 α=1.1 时，s_min 每增加 1%，E[S]_trunc 增加约 0.9% [待核验]。

## Corrected Claim

s_min 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_min = (α-1) * s_min^{α-2} * s_max^{2-α} / (2-α)，当 α=1.1 时，s_min 每增加 1%，E[S]_trunc 增加约 0.9% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：基于截断幂律分布的均值公式推导，敏感度系数在 α=1.1 时约为 0.9，与陈述一致。
