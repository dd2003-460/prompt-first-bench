# N39: Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方差 σ²_S = ∫(s-μ)² f(s)ds (s∈[1KB, 100MB]) 来量化大小分布的离散程度。

## Corrected Claim

Pareto(α=1.1) 分布的二阶矩（方差）为无穷大，导致基于均值的简单相关系数 ρ 失效，必须使用秩相关（Spearman ρ_s ≈ -0.3）或截断方差 σ²_S = ∫(s-μ)² f(s)ds (s∈[1KB, 100MB]) 来量化大小分布的离散程度。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在严重的逻辑依赖和计算冗余。子节点2、3、4并非独立的知识点，而是基于子节点1（解析公式）的连续数值计算步骤（均值->二阶矩->方差->标准差->变异系数）。将它们拆分为4个独立节点破坏了知识单元的内聚性，属于典型的‘过程性冗余’而非概念性正交。此外，子节点4中关于Pearson相关系数失效的论述虽在父节点提及，但在此处仅作为CV值的后果陈述，未深入解释秩相关的必要性，与父节点核心论点（必须使用秩相关）的覆盖略显单薄，主要问题在于冗余。）

## Search Query

Pareto distribution second moment infinite variance alpha 1.1
