# N14: LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布的 CDF，此公式假设无更新且独立请求。

## Corrected Claim

LRU 稳态字节命中率下界近似为 H_LRU ≈ 1 - (1/c) * ∫_0^∞ (1 - F_H(x)) dx，其中 c 为归一化容量，F_H 为热度分布的 CDF，此公式假设无更新且独立请求。

## Evidence

父节点级核验未通过：不完备（子节点正交性良好，分别处理了积分项（热度分布）和容量项（大小-热度相关性）的计算修正，无矛盾或重复。但完备性不足，父节点明确指出了两个关键假设：'无更新'和'独立请求'。子节点仅覆盖了热度分布和容量修正，完全遗漏了关于'无更新'假设的讨论（例如：在存在更新的情况下，LRU公式如何变化或失效，或者需要引入何种修正项），也未涉及'独立请求'假设的适用性边界。）

## Search Query

LRU cache hit rate approximation Pareto workload
