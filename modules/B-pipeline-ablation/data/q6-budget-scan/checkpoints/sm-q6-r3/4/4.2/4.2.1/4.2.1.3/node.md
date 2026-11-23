# N185: 下行带宽成本占比 C_down_ratio 的计算：C_down_ratio = (2000 * 0.22) / (2000 * 0.22 + 200 * 0.

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

下行带宽成本占比 C_down_ratio 的计算：C_down_ratio = (2000 * 0.22) / (2000 * 0.22 + 200 * 0.05) = 440 / (440 + 10) = 97.8%，表明下行带宽成本占总带宽成本的 97.8%，上行成本可忽略不计

## Corrected Claim

下行带宽成本占比 C_down_ratio 的计算：C_down_ratio = (2000 * 0.22) / (2000 * 0.22 + 200 * 0.05) = 440 / (440 + 10) = 97.8%，表明下行带宽成本占总带宽成本的 97.8%，上行成本可忽略不计

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 440/450 ≈ 97.78% 正确，量纲一致，结论符合数值逻辑。
