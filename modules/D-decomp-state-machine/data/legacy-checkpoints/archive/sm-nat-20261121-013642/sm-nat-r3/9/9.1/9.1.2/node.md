# N252: 工作点 2（中频对象，r_i=100 次/天）：LFU 计数器标准差 σ_count ≈ √100 = 10，噪声占比 σ_count/r_i = 10%，处于

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

工作点 2（中频对象，r_i=100 次/天）：LFU 计数器标准差 σ_count ≈ √100 = 10，噪声占比 σ_count/r_i = 10%，处于临界阈值，LFU 误驱逐率约 5%，需结合老化机制（半衰期 1 天）降低噪声累积。

## Corrected Claim

工作点 2（中频对象，r_i=100 次/天）：LFU 计数器标准差 σ_count ≈ √100 = 10，噪声占比 σ_count/r_i = 10%，处于临界阈值，需结合老化机制（半衰期 1 天）降低噪声累积以控制误驱逐率。

## Evidence

[质询]LFU 误驱逐率约 5% 是一个具体的经验性数值，无法仅从标准差和均值直接推导得出，且未提供具体的 LFU 变体（如 Count-Min Sketch 或精确计数器）及容量约束，该数值缺乏理论或实证支撑。 | source=knowledge，逻辑自洽（σ=√100=10 及占比 10% 计算正确），但误驱逐率 5% 为经验事实，缺乏来源直接支持，依据经验事实排除条款降级。
