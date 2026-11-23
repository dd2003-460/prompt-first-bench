# N86: W4A16 (AWQ) 量化在 Qwen3-27B 上的 Perplexity 增加具体值为 1.2% ± 0.4%，基于 LLM-Bench 社区复现数据（3

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

W4A16 (AWQ) 量化在 Qwen3-27B 上的 Perplexity 增加具体值为 1.2% ± 0.4%，基于 LLM-Bench 社区复现数据（32K 上下文）

## Corrected Claim

W4A16 (AWQ) 量化在 Qwen3-27B 上通常会导致 Perplexity 轻微增加，具体数值需依据特定基准测试确定。

## Evidence

[质询]具体数值（1.2% ± 0.4%）及特定基准（LLM-Bench 社区复现）属于经验事实，缺乏来源支持，且不同量化实现或数据集可能导致结果波动，无法排除其他可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B AWQ W4A16 perplexity increase 32K context benchmark
