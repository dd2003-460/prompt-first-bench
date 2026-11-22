# N80: 卖家收入冲击模型：ΔRevenue_seller = (P_new - P_old) * Q_seller，其中 P_new 为展示近期成交价后的预期成交价（收

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

卖家收入冲击模型：ΔRevenue_seller = (P_new - P_old) * Q_seller，其中 P_new 为展示近期成交价后的预期成交价（收敛至 P_avg），P_old 为当前高挂价，Q_seller 为预期成交量。

## Corrected Claim

卖家收入冲击模型：ΔRevenue_seller = (P_new - P_old) * Q_seller，其中 P_new 为展示近期成交价后的预期成交价（收敛至 P_avg），P_old 为当前高挂价，Q_seller 为预期成交量。

## Evidence

父节点级核验未通过：不完备（子节点分别处理了公式中的 Q_seller（数量维度）和 P_new(t)（价格/时间维度），两者定义域不同，无逻辑重叠或矛盾，正交性良好。但完备性不足：父节点中的 P_old 和 P_avg 被视为已知输入，未说明其来源或确定机制；此外，模型假设 Q_seller 在收敛过程中保持恒定（仅由最终价格决定），忽略了价格随时间动态变化对成交量的实时影响（即 Q 也应随 t 变化），导致模型在时间维度上的物理意义不自洽。）
