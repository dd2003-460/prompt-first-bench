# N10: LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) *

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) * (1 - F_H(h(s))) ds，其中 h(s) 由负相关 ρ=-0.3 确定，该积分需数值求解，下界由忽略相关性的独立假设（ρ=0）计算得出。

## Corrected Claim

LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) * (1 - F_H(h(s))) ds，其中 h(s) 由负相关 ρ=-0.3 确定，该积分需数值求解，下界由忽略相关性的独立假设（ρ=0）计算得出。

## Evidence

父节点级核验未通过：不完备（子节点1（解析/简化模型）与子节点2（数值/精确求解方法）在方法论上是正交的，分别对应父节点中提到的‘下界计算’和‘数值求解’两个不同侧面。但存在完备性问题：父节点明确定义了 h(s) 由负相关 ρ=-0.3 确定，而子节点1在 ρ=0 假设下将 h_ref 简化为基于热度的静态阈值，完全忽略了 s 和 h 之间的函数映射关系 h(s)，导致其公式在 ρ≠0 的真实场景下物理意义缺失或错误；此外，子节点2虽然提到了生成联合分布，但未明确说明如何利用该分布去逼近父节点公式中的积分项（即是否通过蒙特卡洛采样还是直接累加期望），逻辑链条略有断裂。）

## Search Query

LRU cache hit rate lower bound pareto size popularity correlation
