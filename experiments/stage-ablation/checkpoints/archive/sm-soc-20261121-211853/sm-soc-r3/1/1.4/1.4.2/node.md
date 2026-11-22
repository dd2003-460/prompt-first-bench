# N28: 触发‘信号筛选’机制的搜索成本占比阈值 $\theta_{sc}$ 为：当 $\frac{C_{total\_search}}{P_{item}} < \the

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

触发‘信号筛选’机制的搜索成本占比阈值 $\theta_{sc}$ 为：当 $\frac{C_{total\_search}}{P_{item}} < \theta_{sc}$ 时，买家转向信号筛选；题面假设 $\theta_{sc} = 5\%$ 需通过 A/B 测试验证，若实测 $\theta_{sc} < 3\%$，则 15-25% 溢价下的搜索成本占比可能仍高于阈值，矛盾解释失效。

## Corrected Claim

触发‘信号筛选’机制的搜索成本占比阈值 $\theta_{sc}$ 需通过 A/B 测试验证。若实测 $\theta_{sc}$ 显著低于假设值（例如从 5% 降至 3% 以下），则在高溢价（如 15-25%）场景下，搜索成本占比可能仍高于阈值，导致基于高阈值假设的矛盾解释失效。

## Evidence

[质询]该陈述包含具体的经验参数（阈值5%、临界值3%、溢价区间15-25%），这些数值并非由第一性原理或数学公理严格推导得出，而是依赖于特定市场环境的实证数据。若缺乏外部来源支持，无法确认这些具体数值在一般情况下的有效性，存在将特定案例参数泛化为通用规则的风险。 | 经验事实，逻辑自洽但缺来源支持。陈述内部逻辑（若实测阈值低于假设值，则原解释失效）成立，但具体数值（5%, 3%, 15-25%）属于经验参数，无外部来源验证，故降级。

## Search Query

threshold search cost ratio price sensitivity signal screening behavior economics experiment
