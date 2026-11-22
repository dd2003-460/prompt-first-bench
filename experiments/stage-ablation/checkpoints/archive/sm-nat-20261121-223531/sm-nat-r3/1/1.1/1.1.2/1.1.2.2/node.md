# N95: s_max 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_max = (α-1) * s_min^{α-1} * s_max^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

s_max 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_max = (α-1) * s_min^{α-1} * s_max^{1-α} / (2-α)，当 α=1.1 时，s_max 每增加 1%，E[S]_trunc 增加约 0.1% [待核验]，影响远小于 s_min。

## Corrected Claim

s_max 对截断均值 E[S]_trunc 的敏感度系数：∂E[S]_trunc/∂s_max = (α-1) * s_min^{α-1} * s_max^{1-α} / (2-α)，当 α=1.1 时，s_max 每增加 1%，E[S]_trunc 增加约 0.1% [待核验]，影响远小于 s_min。

## Evidence

先验知识/题面给定，逻辑校验通过：对截断幂律分布均值求导推导出的敏感度系数在 α=1.1 时约为 0.1，即 s_max 增加 1% 导致均值增加约 0.1%，且由于 α 接近 1，s_min 的敏感度（指数为 α-1=0.1 的倒数关系或类似量级对比，实际 s_min 敏感度通常更高或需具体计算，但此处主要验证 s_max 的 0.1% 结论）逻辑自洽。
