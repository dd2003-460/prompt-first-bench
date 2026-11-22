# N121: 权重 $w_2$ 的确定机制：买家对平台最低成交价 $P_{min}$ 的权重 $w_2$ 取决于买家对‘捡漏’的敏感度 $\lambda_{bargain}$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

权重 $w_2$ 的确定机制：买家对平台最低成交价 $P_{min}$ 的权重 $w_2$ 取决于买家对‘捡漏’的敏感度 $\lambda_{bargain}$ 和 $P_{min}$ 与 $P_{ref}$ 的偏离程度 $D_{min} = \frac{P_{ref} - P_{min}}{P_{ref}}$。若 $D_{min}$ 较大（如 >20%），则 $w_2$ 显著增加，公式为 $w_2 = \lambda_{bargain} \cdot D_{min}$。需确保 $w_1 + w_2 \le 1$，若超过则需归一化。

## Corrected Claim

权重 $w_2$ 的确定机制：买家对平台最低成交价 $P_{min}$ 的权重 $w_2$ 取决于买家对‘捡漏’的敏感度 $\lambda_{bargain}$ 和 $P_{min}$ 与 $P_{ref}$ 的偏离程度 $D_{min} = \frac{P_{ref} - P_{min}}{P_{ref}}$。若 $D_{min}$ 较大（如 >20%），则 $w_2$ 显著增加，公式为 $w_2 = \lambda_{bargain} \cdot D_{min}$。需确保 $w_1 + w_2 \le 1$，若超过则需归一化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

bargain hunting sensitivity minimum price anchor buyer valuation
