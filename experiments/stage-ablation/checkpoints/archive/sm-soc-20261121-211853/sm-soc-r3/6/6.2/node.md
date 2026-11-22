# N60: 信号可信度对决策时间的非线性影响：买家决策时间 T_decision = T_base × (1 - 0.3 × ln(C))，当 C 从 1.0 增至 1.2

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N23

## Claim

信号可信度对决策时间的非线性影响：买家决策时间 T_decision = T_base × (1 - 0.3 × ln(C))，当 C 从 1.0 增至 1.25 时，T_decision 缩短 7.2%；当 C 从 1.25 增至 1.5 时，T_decision 仅缩短 2.1%，存在边际效用递减。

## Corrected Claim

在特定模型假设下，信号可信度对决策时间的影响呈现非线性特征，随着可信度C的增加，决策时间缩短的边际效用递减。

## Evidence

父节点级核验未通过：不完备（子节点分别解释了公式中的基准项 T_base 和系数 0.3，两者正交且不冗余。但父节点明确描述了‘边际效用递减’这一核心非线性特征（即 C 从 1.0->1.25 缩短 7.2%，1.25->1.5 仅缩短 2.1%），而子节点仅解释了系数来源和基准定义，未单独解释为何该公式结构会导致边际效用递减（即二阶导数性质或具体数值验证），导致对父节点核心结论的机制覆盖不完备。）

## Search Query

price signal credibility decision time nonlinear effect consumer behavior
