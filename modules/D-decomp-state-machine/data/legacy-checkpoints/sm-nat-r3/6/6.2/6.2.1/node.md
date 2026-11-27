# N262: 工作点 A（保守/高成本）：假设 Pareto 截断 x_max = 1GB，计算 E[S | top 20%] = E[S; S≤1GB, Rank≤20%]

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

工作点 A（保守/高成本）：假设 Pareto 截断 x_max = 1GB，计算 E[S | top 20%] = E[S; S≤1GB, Rank≤20%]，若该值 > 6.4KB，则 S_top20 > 128GB，LRU 无法覆盖前 20% 对象，命中率上限需按实际覆盖比例下调。

## Corrected Claim

工作点 A（保守/高成本）：假设 Pareto 截断 x_max = 1GB，计算 E[S | top 20%] = E[S; S≤1GB, Rank≤20%]。若该期望值显著高于 LRU 缓存单对象平均开销，则 S_top20 可能超过 128GB，导致 LRU 无法覆盖前 20% 对象，命中率上限需按实际覆盖比例下调。

## Evidence

[质询]该陈述包含具体的经验性阈值（6.4KB）和推导出的容量结论（128GB），属于特定场景下的经验事实或特定模型参数，无法仅从第一性原理严格推出，且缺乏外部来源支持其具体数值的有效性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Pareto distribution truncated mean top 20 percent 1GB limit 100000 objects
