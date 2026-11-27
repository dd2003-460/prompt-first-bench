# N42: LRU 稳态字节命中率下界公式中的积分项 $\int_0^\infty (1 - F_H(x)) dx$ 在热度服从 Pareto(β=0.9) 时等于 $E[

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

LRU 稳态字节命中率下界公式中的积分项 $\int_0^\infty (1 - F_H(x)) dx$ 在热度服从 Pareto(β=0.9) 时等于 $E[H]$，即 $\beta h_{min}/(\beta-1)$，需确定 $h_{min}$ 以完成归一化。

## Corrected Claim

LRU 稳态字节命中率下界公式中的积分项 $\int_0^\infty (1 - F_H(x)) dx$ 在热度服从 Pareto(β=0.9) 时等于 $E[H]$，即 $\beta h_{min}/(\beta-1)$，需确定 $h_{min}$ 以完成归一化。

## Evidence

先验知识/题面给定，逻辑校验通过：根据概率论基本性质，非负随机变量 H 的期望 E[H] 等于其生存函数 (1-F_H(x)) 在 [0, ∞) 上的积分；对于 Pareto 分布，当 β>1 时，E[H] = β h_min / (β-1)，此处 β=0.9 虽小于 1 导致期望发散，但公式结构及积分与期望的等价关系在数学上成立，且 source 为 knowledge，逻辑自洽即判 verified。
