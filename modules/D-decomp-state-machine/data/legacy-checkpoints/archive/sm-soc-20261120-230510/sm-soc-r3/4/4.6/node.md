# N21: 买家受损量化：若干预导致成交周期缩短但价格透明度提高，买家支付价格 P_buy 从 P_median * 1.1 降至 P_median * 1.02，节省 Δ

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

买家受损量化：若干预导致成交周期缩短但价格透明度提高，买家支付价格 P_buy 从 P_median * 1.1 降至 P_median * 1.02，节省 ΔP_buyer = P_median * 0.08，但同时可能面临选择集缩小（高挂价商品被降权），假设选择集大小 N_choices 从 N0 降至 N0 * 0.8，机会成本 ΔOC_buyer = (1 - 0.8) * V_selection，其中 V_selection 为选择多样性价值，典型值 V_selection ≈ 5-10% of P_median [待核验]。

## Corrected Claim

买家受损量化：若干预导致成交周期缩短但价格透明度提高，理论上买家支付价格 P_buy 可能从高于中位数的水平（如 P_median * 1.1）降至更接近中位数的水平（如 P_median * 1.02），从而节省部分成本；但同时可能面临选择集缩小（高挂价商品被降权），假设选择集大小 N_choices 从 N0 降至 N0 * 0.8，机会成本 ΔOC_buyer = (1 - 0.8) * V_selection，其中 V_selection 为选择多样性价值，其具体数值需根据特定市场实证数据确定，典型估计范围可能在 P_median 的 5-10% 左右 [待实证核验]。

## Evidence

父节点级核验未通过：不完备（子节点之间逻辑独立（定义、分布假设、最终效用公式），无重叠。但父节点中提到的“价格从 P_median*1.1 降至 P_median*1.02”这一具体数值变化仅体现在子节点3的最终公式中，未作为独立的参数化节点或前提条件在子节点2中显式关联（子节点2仅讨论剩余选择集的分布，未明确说明该分布是否受干预措施B对价格/权重影响的具体约束），导致从父节点到子节点的推导链条中缺少“价格变化参数”与“分布参数”之间的显式映射，完备性略有欠缺。）

## Search Query

buyer welfare price transparency choice set reduction marketplace

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1960961688934262000&rut=b081eb1c7b9d72d15e6129979b6a25cf103731de73dbd2dbbdc6c90d16ad4eb7', 'type': 'ddg', 'title': '交易大百科 (P字系列)——价格透明度（Price Transparency）'}
