# N62: LRU 稳态命中率公式在 β=0.9 重尾分布下的适用性约束：经典 Belady 最优替换假设要求请求序列独立同分布（i.i.d.），但 Pareto(β<1)

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

LRU 稳态命中率公式在 β=0.9 重尾分布下的适用性约束：经典 Belady 最优替换假设要求请求序列独立同分布（i.i.d.），但 Pareto(β<1) 导致自相关系数 ρ_auto > 0.3，此时 LRU 命中率下界需乘以修正因子 1/(1+ρ_auto)，其中 ρ_auto 由请求间隔分布的方差/均值比估算。

## Corrected Claim

在重尾分布（如 Pareto）下，请求序列可能表现出自相关性，经典 i.i.d. 假设下的 LRU 命中率公式可能需要引入修正因子以反映自相关性的影响，但具体的修正公式（如 1/(1+ρ_auto)）和阈值（ρ_auto > 0.3）依赖于特定的模型假设或实验数据，并非通用理论结论。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点N62-1关注ρ_auto的量化推导与定义（如何从模型得出数值），子节点N62-2关注修正因子公式本身的适用边界与非线性修正（数值得出后如何应用）。两者分别解决了'值从何来'和'公式是否有效'两个正交问题，无重复或矛盾。父节点包含两个核心要素：ρ_auto的定义/估算方法和修正因子1/(1+ρ_auto)的适用性，两个子节点恰好分别覆盖这两点，具备完备性。）

## Search Query

LRU cache hit rate heavy-tailed workload self-correlation correction factor
