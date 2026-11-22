# N81: 计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto(α=1.1)，s_min 通常设为 1KB 或 1MB

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto(α=1.1)，s_min 通常设为 1KB 或 1MB 以匹配 CDN 对象特征，对于 Pareto(β=0.9)，f_min 由总请求数 50M 和对象数 100k 归一化得出

## Corrected Claim

计算条件概率 P(size > s | freq > f) 需先确定边缘分布的截断点：对于 Pareto 分布，s_min 和 f_min 需根据具体的 CDN 对象特征及总请求数/对象数进行归一化设定，具体数值（如 1KB/1MB）取决于实际数据集的统计特性。

## Evidence

[质询]该陈述包含具体的工程经验参数（如 s_min 设为 1KB/1MB，β=0.9 等），属于经验事实而非第一性原理可推导的数学性质。在缺乏外部来源支持的情况下，无法确认这些具体数值是行业标准还是任意假设，存在口径混淆或来源不可靠的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Pareto distribution truncation point CDN object size request frequency normalization
