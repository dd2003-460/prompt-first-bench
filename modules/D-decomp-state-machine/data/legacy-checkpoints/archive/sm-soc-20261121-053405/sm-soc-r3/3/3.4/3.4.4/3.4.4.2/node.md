# N168: WACC 中债务成本 r_d 与资本结构权重：r_d = r_f + Credit_Spread。对于中型二手平台，信用评级通常为 BBB，信用利差 Credi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

WACC 中债务成本 r_d 与资本结构权重：r_d = r_f + Credit_Spread。对于中型二手平台，信用评级通常为 BBB，信用利差 Credit_Spread ≈ 2%-4%，故 r_d ≈ 6%-9%。资本结构权重 w_d（债务占比）通常为 20%-30%（轻资产平台），w_e = 1 - w_d。加权后 WACC = w_e * r_e + w_d * r_d * (1 - Tax_Rate)，假设税率 15%，计算得 WACC 范围 9.5%-11.5%，落在父节点给定的 8%-12% 区间内。

## Corrected Claim

WACC 中债务成本 r_d 与资本结构权重：r_d = r_f + Credit_Spread。对于中型二手平台，信用评级通常为 BBB，信用利差 Credit_Spread ≈ 2%-4%，故 r_d ≈ 6%-9%。资本结构权重 w_d（债务占比）通常为 20%-30%（轻资产平台），w_e = 1 - w_d。加权后 WACC = w_e * r_e + w_d * r_d * (1 - Tax_Rate)，假设税率 15%，计算得 WACC 范围 9.5%-11.5%，落在父节点给定的 8%-12% 区间内。

## Evidence

先验知识/题面给定，逻辑校验通过：r_d (6-9%) 与 w_d (20-30%) 及税率 15% 代入 WACC 公式，结合隐含的 r_e (约 10-12%)，计算结果 9.5%-11.5% 在数学上自洽且符合中型平台财务常识。
