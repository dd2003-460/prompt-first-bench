# N100: 日间 8 小时运行场景下的年度电力成本：T_hours = 8h/day * 365 days = 2920h。若 E_price = $0.15/kWh，ΔC

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

日间 8 小时运行场景下的年度电力成本：T_hours = 8h/day * 365 days = 2920h。若 E_price = $0.15/kWh，ΔC_power_year = 0.428 kW * 2920 h * $0.15/kWh ≈ $187.2/year。

## Corrected Claim

日间 8 小时运行场景下的年度电力成本：T_hours = 8h/day * 365 days = 2920h。若 E_price = $0.15/kWh，ΔC_power_year = 0.428 kW * 2920 h * $0.15/kWh ≈ $187.2/year。

## Evidence

父节点级核验未通过：不完备（子节点1（3年累计成本）和子节点2（盈亏平衡溢价）在逻辑上是递进关系而非正交（独立）关系，子节点2直接依赖子节点1的结果。此外，父节点仅提供了年度成本计算，子节点引入了'3年周期'和'硬件溢价'这一父节点未明确提及的关键假设/维度，导致分解超出了父节点的定义范围，且未覆盖父节点中隐含的'与其他场景对比'或'敏感性分析'等潜在方面（如果父节点意图是全面评估）。）
