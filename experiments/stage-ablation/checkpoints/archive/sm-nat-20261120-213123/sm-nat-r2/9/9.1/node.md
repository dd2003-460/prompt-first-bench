# N72: LRU 稳态驻留对象数量 k_eff 的确定公式：k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)，其中 S_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N27

## Claim

LRU 稳态驻留对象数量 k_eff 的确定公式：k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)，其中 S_{(i)} 为按热度排序后第 i 个对象的大小。由于 ρ=-0.3，热度 Top-k 对象的大小分布 E[S | H=Top-k] 低于总体均值 E[S]，需计算条件期望 E[S|H>h_k] 来修正 k_eff 的实际值，而非直接使用 N26 中的平均大小估计。

## Corrected Claim

LRU 稳态驻留对象数量 k_eff 的确定公式为 k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)。在热度与大小存在负相关（如 ρ=-0.3）的场景下，Top-k 对象的大小分布低于总体均值，需通过计算条件期望 E[S|H>h_k] 来修正 k_eff 的实际值，而非直接使用平均大小估计。

## Evidence

[质询]该陈述包含具体的经验参数（ρ=-0.3）和特定的统计修正逻辑，属于经验事实/模型假设，无法仅从第一性原理推导，且缺乏外部来源支持其具体数值和因果关系的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LRU cache steady state object count size dependent on popularity correlation Pareto distribution
