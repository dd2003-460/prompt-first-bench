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

父节点级核验未通过：不完备（子节点之间正交，分别讨论了积分项在特定分布下的计算和容量参数在相关性下的修正，无重复或矛盾。但完备性不足：父节点公式包含三个关键要素（积分项、容量c、假设条件），子节点1仅处理了积分项在Pareto分布下的特例，未涵盖一般情况；子节点2处理了容量c的修正，但子节点1未提及热度分布的一般性积分计算，且两者均未明确说明‘无更新且独立请求’这一假设在修正后的适用性或限制。）

## Search Query

LRU cache hit rate approximation Pareto workload
