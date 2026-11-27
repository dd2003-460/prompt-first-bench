# N82: 买家总效用变化 ΔU_buyer 的完整表达式：ΔU_buyer = (P_median * 0.08) - (0.2 * V_selection)，其中第一项

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

买家总效用变化 ΔU_buyer 的完整表达式：ΔU_buyer = (P_median * 0.08) - (0.2 * V_selection)，其中第一项为价格节省收益，第二项为选择集缩小导致的机会成本损失，需验证在典型参数下 ΔU_buyer > 0 的条件。

## Corrected Claim

买家总效用变化 ΔU_buyer 的完整表达式：ΔU_buyer = (P_median * 0.08) - (0.2 * V_selection)，其中第一项为价格节省收益，第二项为选择集缩小导致的机会成本损失，需验证在典型参数下 ΔU_buyer > 0 的条件。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点结构清晰且逻辑互补：第一个子节点提供通用的临界条件（理论边界），后两个子节点分别验证了该条件两侧的具体数值案例（正效用与负效用）。三者分别对应‘通用推导’、‘有利情形’和‘不利情形’，互不重叠且共同构成了对父节点‘验证条件’要求的完整覆盖。工作点1和2虽然形式相似，但代表了参数空间的不同区域（V_selection < 0.4P_median 与 > 0.4P_median），并非简单的参数重复，而是为了展示不同买家群体的不同结果，因此不构成冗余。）
