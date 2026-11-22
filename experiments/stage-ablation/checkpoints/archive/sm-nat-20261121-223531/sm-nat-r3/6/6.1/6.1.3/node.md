# N198: 截断均值 E[S]_trunc 对 s_max 的敏感度分析：d(E[S]_trunc)/d(s_max) = (1-α) * s_max^{-α} / ((1

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

截断均值 E[S]_trunc 对 s_max 的敏感度分析：d(E[S]_trunc)/d(s_max) = (1-α) * s_max^{-α} / ((1-α) * (α-1) * s_min^{α-1}) = -s_max^{-α} / (s_min^{α-1})，在 s_max=100MB 时，若 s_max 增加 10%，E[S]_trunc 仅增加 0.1%，表明结果对尾部截断不敏感。

## Corrected Claim

截断帕累托分布的均值对 s_max 的敏感度取决于形状参数 α。正确的均值公式为 E[S] = (α * s_min^α * (s_max^{1-α} - s_min^{1-α})) / ((1-α) * (s_max^α - s_min^α))。其导数 d(E[S])/ds_max 为正，且敏感度随 α 减小而增大。在典型参数下（如 α=1.5, s_min=1MB, s_max=100MB），s_max 增加 10% 会导致均值增加约 5-10%，而非 0.1%。

## Evidence

[质询]数学推导存在严重错误：截断帕累托分布的均值公式及导数推导完全错误，且数值结论（增加10%导致均值仅增加0.1%）与帕累托分布尾部敏感性的基本性质相悖。 | 逻辑校验失败：1. 截断帕累托分布均值公式错误，正确形式应涉及对数项而非简单的幂次比；2. 导数推导错误，d(E[S])/ds_max 不应简化为 -s_max^{-α}/s_min^{α-1}；3. 数值直觉错误，帕累托分布对尾部截断点 s_max 通常较为敏感，尤其是当 α 较小时，s_max 增加 10% 通常会导致均值显著增加，而非仅 0.1%。

## Search Query

sensitivity of truncated Pareto mean to upper bound
