# N55: Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得 S_1% ≈ 1KB * (0.99)^(-10) ≈ 1.1KB，需验证该阈值下 Top 1% 对象的实际字节占比

## Corrected Claim

Top 1% 对象阈值大小 S_1% 的计算：S_1% = S_min * (1 - 0.01)^(1/(1-α))，代入 α=1.1, S_min=1KB 得 S_1% ≈ 1KB * (0.99)^(-10) ≈ 1.1KB，需验证该阈值下 Top 1% 对象的实际字节占比

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)

## Search Query

Pareto distribution quantile formula alpha=1.1
