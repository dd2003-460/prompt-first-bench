# N114: 混合策略下自建部分需预留的回源带宽冗余 B_redundant = Peak_Backhaul_Traffic * Safety_Factor，其中 Safet

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

混合策略下自建部分需预留的回源带宽冗余 B_redundant = Peak_Backhaul_Traffic * Safety_Factor，其中 Safety_Factor 通常取 1.5-2.0，以吸收 H(t) 降至 70% 时的瞬时流量峰值。

## Corrected Claim

混合策略下自建部分需预留的回源带宽冗余 B_redundant = Peak_Backhaul_Traffic * Safety_Factor，其中 Safety_Factor 通常取 1.5-2.0，以吸收 H(t) 降至 70% 时的瞬时流量峰值。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应公式中的核心变量（Peak_Backhaul_Traffic）、调节参数（Safety_Factor）以及最终的经济/工程决策（机会成本/计费模式），维度清晰，无逻辑重叠。子节点1完成了具体数值推导，子节点2分析了参数敏感性，子节点3引入了成本优化视角，共同构成了完整的决策链。）
