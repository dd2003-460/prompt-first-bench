# N249: C_hw_5090 的敏感性分析：当配件成本 C_peripheral 在 $800-$1080 区间波动（基于 N112-N114 的修正）时，C_hw_50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

C_hw_5090 的敏感性分析：当配件成本 C_peripheral 在 $800-$1080 区间波动（基于 N112-N114 的修正）时，C_hw_5090 的范围为 $3000-$3280；该不确定性区间需代入 N113 的 TCO 交叉点公式，重新计算与 2×4090 方案的电价平衡点，以评估推荐方案的鲁棒性。

## Corrected Claim

C_hw_5090 的敏感性分析：当配件成本 C_peripheral 在 $800-$1080 区间波动（基于 N112-N114 的修正）时，C_hw_5090 的范围为 $3000-$3280；该不确定性区间需代入 N113 的 TCO 交叉点公式，重新计算与 2×4090 方案的电价平衡点，以评估推荐方案的鲁棒性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sensitivity analysis hardware cost uncertainty TCO cross-over point
