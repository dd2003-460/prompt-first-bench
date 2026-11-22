# N26: 干预建议置信度：最小干预策略的有效性置信度取决于策略实施前后均衡点的移动幅度 ΔEquilibrium，量化为挂价-成交价差从20%降至10%所需的策略强度 S

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

干预建议置信度：最小干预策略的有效性置信度取决于策略实施前后均衡点的移动幅度 ΔEquilibrium，量化为挂价-成交价差从20%降至10%所需的策略强度 S_min，若 S_min > 0.5（归一化）则置信度低，因可能引发卖家流失。

## Corrected Claim

最小干预策略的有效性评估需考虑策略实施前后均衡点的移动幅度 ΔEquilibrium。量化指标如挂价-成交价差从20%降至10%所需的策略强度 S_min 可作为参考，若 S_min 较高（如 > 0.5，归一化），可能因引发卖家流失而增加策略实施的不确定性或风险，从而降低对策略长期有效性的信心。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了核心变量 S_min、风险指标（卖家流失/置信度阈值）和效果验证指标（均衡移动），三者逻辑独立且互补，共同构成了父节点中‘置信度取决于...’的完整评估框架，无重复或矛盾。）

## Search Query

equilibrium shift magnitude minimal intervention marketplace seller churn
