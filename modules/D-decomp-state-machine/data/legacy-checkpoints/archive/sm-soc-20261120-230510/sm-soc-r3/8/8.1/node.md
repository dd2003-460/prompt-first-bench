# N99: 高挂价卖家边际伤害率 MH_seller 的分解：MH_seller = (1 - w_new/w_old) × (1 - Prob(Sell|w_new)/P

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N31

## Claim

高挂价卖家边际伤害率 MH_seller 的分解：MH_seller = (1 - w_new/w_old) × (1 - Prob(Sell|w_new)/Prob(Sell|w_old))，其中 w_new/w_old = 0.5（基于N18的权重减半假设），Prob(Sell) 的变化率取决于流量-转化弹性 ε_flow，典型值 ε_flow ∈ [0.8, 1.2]。

## Corrected Claim

高挂价卖家边际伤害率 MH_seller 的分解：MH_seller = (1 - w_new/w_old) × (1 - Prob(Sell|w_new)/Prob(Sell|w_old))，其中 w_new/w_old = 0.5（基于N18的权重减半假设），Prob(Sell) 的变化率取决于流量-转化弹性 ε_flow，典型值 ε_flow ∈ [0.8, 1.2]。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上正交且覆盖了父节点定义的关键参数范围（ε_flow），但本质上是对同一公式中单一变量（ε_flow）的三个不同取值进行的场景枚举，属于高度冗余的参数扫描，而非结构性的独立分解。）
