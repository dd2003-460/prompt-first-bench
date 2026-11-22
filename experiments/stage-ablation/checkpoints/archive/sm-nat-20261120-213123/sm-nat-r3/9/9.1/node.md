# N72: LRU 稳态驻留对象数量 k_eff 的确定公式：k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)，其中 S_

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

LRU 稳态驻留对象数量 k_eff 的确定公式：k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)，其中 S_{(i)} 为按热度排序后第 i 个对象的大小。由于 ρ=-0.3，热度 Top-k 对象的大小分布 E[S | H=Top-k] 低于总体均值 E[S]，需计算条件期望 E[S|H>h_k] 来修正 k_eff 的实际值，而非直接使用 N26 中的平均大小估计。

## Corrected Claim

LRU 稳态驻留对象数量 k_eff 的确定公式为 k_eff = min(N, max_k | Σ_{i=1}^{k} S_{(i)} ≤ C |)。在热度与大小存在负相关（如 ρ=-0.3）的场景下，Top-k 对象的大小分布低于总体均值，需通过计算条件期望 E[S|H>h_k] 来修正 k_eff 的实际值，而非直接使用平均大小估计。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点A和B本质上是在计算同一个公式 k_eff = min(N, C/E[S_cond])，只是代入的条件期望 E[S] 不同（全局均值 vs 条件均值）。它们不是正交的不同方面，而是同一逻辑分支下的不同参数取值，因此存在冗余。此外，父节点核心在于“修正 k_eff 的实际值”，但子节点A、B、C的结论都指向 k_eff=N（即缓存未饱和），未能覆盖父节点隐含的另一种关键情况：当负相关导致热门对象足够小，使得 C 无法容纳所有 N 个对象时（即 k_eff < N 的情况），这才是 LRU 稳态分析中真正需要确定具体 k_eff 公式应用场景的核心。当前分解缺失了“容量受限（k_eff < N）”这一关键分支的推导或验证。）

## Search Query

LRU cache steady state object count size dependent on popularity correlation Pareto distribution
