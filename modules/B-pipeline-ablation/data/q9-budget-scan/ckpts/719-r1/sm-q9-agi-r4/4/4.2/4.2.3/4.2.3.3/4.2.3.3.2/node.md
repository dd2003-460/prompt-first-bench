# N613: Pooled Standard Deviation的计算修正：在配对设计中，Cohen's d的分母应为差值序列的标准差S_D，而非合并标准差，即d = mea

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N218

## Claim

Pooled Standard Deviation的计算修正：在配对设计中，Cohen's d的分母应为差值序列的标准差S_D，而非合并标准差，即d = mean(D) / std(D)，以避免高估效应量

## Corrected Claim

Pooled Standard Deviation的计算修正：在配对设计中，Cohen's d的分母应为差值序列的标准差S_D，而非合并标准差，即d = mean(D) / std(D)，以避免高估效应量

## Evidence

先验知识/题面给定，逻辑校验通过：在配对样本t检验中，效应量Cohen's dz的定义即为差值均值除以差值标准差，使用合并标准差会忽略配对相关性导致分母偏大从而低估效应量（而非高估，但核心逻辑是必须用S_D），该陈述关于分母应为S_D的核心主张符合统计学定义。
