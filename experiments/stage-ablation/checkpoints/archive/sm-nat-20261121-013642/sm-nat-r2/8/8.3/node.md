# N86: 重尾分布下 LRU 下界过低的修正因子 κ = H_LRU_corrected / H_LRU_lower，κ 通常介于 1.1 到 1.5 之间，具体值取决于

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

重尾分布下 LRU 下界过低的修正因子 κ = H_LRU_corrected / H_LRU_lower，κ 通常介于 1.1 到 1.5 之间，具体值取决于 α 和缓存容量 C 相对于对象大小分布中位数的比值

## Corrected Claim

重尾分布下 LRU 下界通常偏低，存在修正因子 κ = H_LRU_corrected / H_LRU_lower，其具体数值取决于 α 和缓存容量 C 相对于对象大小分布中位数的比值，但具体范围需依据特定实验数据或文献确定。

## Evidence

[质询]该陈述包含具体的经验数值范围（1.1-1.5）和特定的修正因子定义，属于经验事实而非第一性原理可推导的数学恒等式。在缺乏外部来源支持的情况下，无法确认该特定数值区间和定义是否为业界公认标准或特定论文结论，存在口径混淆或数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

cache hit rate correction factor heavy-tailed distribution LRU lower bound
