# N36: ‘可发表级’结论的量化验证标准之一为统计显著性检验的 p-value < 0.05 且效应量 Cohen's d > 0.2。对于 AI 生成的实验代码，若未内

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

‘可发表级’结论的量化验证标准之一为统计显著性检验的 p-value < 0.05 且效应量 Cohen's d > 0.2。对于 AI 生成的实验代码，若未内置自动统计检验模块（如 scipy.stats.ttest_ind），则需人工介入检查。假设人工检查耗时 5 分钟/次，而 AI 自主循环目标为 10 分钟/次，则人工干预率必须低于 50% 才能满足‘无需人类逐步指导’的效率约束。

## Corrected Claim

‘可发表级’结论的量化验证标准之一为统计显著性检验的 p-value < 0.05 且效应量 Cohen's d > 0.2。对于 AI 生成的实验代码，若未内置自动统计检验模块（如 scipy.stats.ttest_ind），则需人工介入检查。假设人工检查耗时 5 分钟/次，而 AI 自主循环目标为 10 分钟/次，则人工干预率必须低于 50% 才能满足‘无需人类逐步指导’的效率约束。

## Evidence

检索失败: no sources from any channel (all 5 failed)
