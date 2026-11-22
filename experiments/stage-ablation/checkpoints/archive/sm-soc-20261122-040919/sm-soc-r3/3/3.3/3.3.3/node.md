# N75: 下游投影2：买家期望效用 E[U_buyer] 的福利变化分解。ΔE[U_buyer] = ΔE[Value] - ΔE[Price] - ΔE[Search_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

下游投影2：买家期望效用 E[U_buyer] 的福利变化分解。ΔE[U_buyer] = ΔE[Value] - ΔE[Price] - ΔE[Search_Cost]。其中 ΔE[Price] < 0（因溢价降低），ΔE[Search_Cost] 符号不定（短期可能 >0，长期 <0）。若 ΔE[Value] 的改善幅度 > |ΔE[Price]| + max(ΔE[Search_Cost])，则买家整体福利为正。需量化各分项的具体贡献度。

## Corrected Claim

下游投影2：买家期望效用 E[U_buyer] 的福利变化分解。ΔE[U_buyer] = ΔE[Value] - ΔE[Price] - ΔE[Search_Cost]。其中 ΔE[Price] < 0（因溢价降低），ΔE[Search_Cost] 符号不定（短期可能 >0，长期 <0）。若 ΔE[Value] 的改善幅度 > |ΔE[Price]| + max(ΔE[Search_Cost])，则买家整体福利为正。需量化各分项的具体贡献度。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点分解式中的三个核心分项（Value, Price, Search_Cost）及总式定义，彼此独立且无重叠。虽然第一个子节点重述了总公式，但作为定义性节点是必要的，不构成实质性冗余。所有关键方面（各分项量化、时间依赖性、整体福利条件）均被覆盖。）
