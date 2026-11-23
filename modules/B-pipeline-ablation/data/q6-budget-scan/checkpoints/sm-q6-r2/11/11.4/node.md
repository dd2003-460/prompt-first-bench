# N146: 公式中的系数 1.5 和常数 5ms 是经验值，未明确物理意义。更严谨的估算应基于具体网络拓扑：$T_{target} = \alpha_{core} \tim

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

公式中的系数 1.5 和常数 5ms 是经验值，未明确物理意义。更严谨的估算应基于具体网络拓扑：$T_{target} = \alpha_{core} \times (L_{edge} + L_{backhaul, core}) + \alpha_{tail} \times (L_{edge} + L_{backhaul, tail})$，其中 $\alpha_{core}=0.9, \alpha_{tail}=0.1$。

## Corrected Claim

公式中的系数 1.5 和常数 5ms 是经验值，未明确物理意义。更严谨的估算应基于具体网络拓扑：$T_{target} = \alpha_{core} \times (L_{edge} + L_{backhaul, core}) + \alpha_{tail} \times (L_{edge} + L_{backhaul, tail})$，其中 $\alpha_{core}=0.9, \alpha_{tail}=0.1$。

## Evidence

先验知识/题面给定，逻辑校验通过
