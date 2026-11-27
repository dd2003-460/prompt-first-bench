# N351: ETDW 公式中 Power_Efficiency_Factor (PEF) 的计算实例：以 2x RTX 4090 方案为例，Peak_TDP = 2 * 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N126

## Claim

ETDW 公式中 Power_Efficiency_Factor (PEF) 的计算实例：以 2x RTX 4090 方案为例，Peak_TDP = 2 * 450W = 900W；实际平均功耗 (Idle 50% + Load 50%) 约为 2 * (150W + 400W) / 2 = 550W (假设负载因子 0.5)。则 PEF = 900 / 550 ≈ 1.636。该因子用于修正 TCO 中的电费项，反映硬件在低负载下的能效优势。

## Corrected Claim

ETDW 公式中 Power_Efficiency_Factor (PEF) 的计算实例：以 2x RTX 4090 方案为例，Peak_TDP = 2 * 450W = 900W；实际平均功耗 (Idle 50% + Load 50%) 约为 2 * (150W + 400W) / 2 = 550W (假设负载因子 0.5)。则 PEF = 900 / 550 ≈ 1.636。该因子用于修正 TCO 中的电费项，反映硬件在低负载下的能效优势。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（900/550≈1.636），PEF定义符合能效修正因子的常规逻辑（峰值/平均），量级合理。
