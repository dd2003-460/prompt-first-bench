# N174: 参数敏感性分析：对 ESS 约束条件中的 α 和 T_high 进行一阶偏导数分析，∂E(Resident)/∂α = -T_high * (P_ask_hig

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

参数敏感性分析：对 ESS 约束条件中的 α 和 T_high 进行一阶偏导数分析，∂E(Resident)/∂α = -T_high * (P_ask_high - C) * exp(-α*T_high)，∂E(Resident)/∂T_high = -α * (P_ask_high - C) * exp(-α*T_high)；当 α 从 0.01 增加至 0.02 时，T_high 的临界值从 18.4 天降至 9.2 天，表明时间贴现率升高会显著收紧 ESS 成立条件。

## Corrected Claim

参数敏感性分析：对 ESS 约束条件中的 α 和 T_high 进行一阶偏导数分析，∂E(Resident)/∂α = -T_high * (P_ask_high - C) * exp(-α*T_high)，∂E(Resident)/∂T_high = -α * (P_ask_high - C) * exp(-α*T_high)；当 α 从 0.01 增加至 0.02 时，T_high 的临界值从 18.4 天降至 9.2 天，表明时间贴现率升高会显著收紧 ESS 成立条件。

## Evidence

先验知识/题面给定，逻辑校验通过：偏导数符号与量纲符合经济学直觉（贴现率α或高收益持续时间T_high增加均降低驻留期望收益），临界值随α加倍而减半符合指数衰减模型的一阶近似逻辑。
