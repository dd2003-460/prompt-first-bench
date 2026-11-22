# N62: 折现率与NPV计算参数：折现率 \(r\) 取平台加权平均资本成本WACC（估计值 8%-12%），NPV计算公式中 \(\Delta Rev_t = Comm

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

折现率与NPV计算参数：折现率 \(r\) 取平台加权平均资本成本WACC（估计值 8%-12%），NPV计算公式中 \(\Delta Rev_t = Commission \times \Delta GMV_t\)，需明确Commission率（通常2%-5%）及现金流时间步长（月度或季度），以计算净现值 \(NPV = \sum_{t=1}^{T} \frac{\Delta Rev_t}{(1+r)^t}\)。

## Corrected Claim

折现率与NPV计算参数：折现率 \(r\) 取平台加权平均资本成本WACC（估计值 8%-12%），NPV计算公式中 \(\Delta Rev_t = Commission \times \Delta GMV_t\)，需明确Commission率（通常2%-5%）及现金流时间步长（月度或季度），以计算净现值 \(NPV = \sum_{t=1}^{T} \frac{\Delta Rev_t}{(1+r)^t}\)。

## Evidence

先验知识/题面给定，逻辑校验通过：WACC作为折现率、NPV公式结构及佣金率量级均符合财务估值基本逻辑与常识。
