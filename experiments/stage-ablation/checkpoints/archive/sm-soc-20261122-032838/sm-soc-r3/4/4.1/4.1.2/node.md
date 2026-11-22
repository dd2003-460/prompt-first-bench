# N78: 损失厌恶对卖家定价的量化贡献：卖家因损失厌恶（系数 $\lambda_{loss} \approx 2.25$）而设定高于保留价 $C_{hold}$ 的挂价，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

损失厌恶对卖家定价的量化贡献：卖家因损失厌恶（系数 $\lambda_{loss} \approx 2.25$）而设定高于保留价 $C_{hold}$ 的挂价，溢价幅度 $\Delta_{loss} = \lambda_{loss} \times (P_{ref} - C_{hold}) \times \gamma$，其中 $\gamma$ 为风险厌恶程度。若 $\gamma = 0.1$，则损失厌恶贡献约2.25%的溢价，不足以单独解释15-25%的总溢价

## Corrected Claim

损失厌恶对卖家定价的量化贡献：卖家因损失厌恶（系数 $\lambda_{loss} \approx 2.25$）而设定高于保留价 $C_{hold}$ 的挂价，溢价幅度 $\Delta_{loss} = \lambda_{loss} \times (P_{ref} - C_{hold}) \times \gamma$，其中 $\gamma$ 为风险厌恶程度。若 $\gamma = 0.1$，则损失厌恶贡献约2.25%的溢价，不足以单独解释15-25%的总溢价

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于参数定义与基准情境（平均卖家，gamma=0.1），子节点2聚焦于参数区间与极端情境（保守卖家，gamma=0.3）。两者通过不同的gamma取值和对应的结论（4.5% vs 13.5%）互补，共同覆盖了父节点中'不足以单独解释'到'在极端情况下可解释大部分'的完整逻辑链条，且无重复或矛盾。）

## Search Query

loss aversion coefficient impact on seller asking price premium
