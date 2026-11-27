# N197: 基准工作点（B2）：当前均衡下的 Deadweight Loss (DWL) 量化公式 DWL = ∫_{P_market}^{P_ask} (D(P) - S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

基准工作点（B2）：当前均衡下的 Deadweight Loss (DWL) 量化公式 DWL = ∫_{P_market}^{P_ask} (D(P) - S(P)) dP，在假设 D(P) 和 S(P) 为线性函数且斜率分别为 -b_d 和 b_s 的简化模型下，DWL 可解析为 (P_ask - P_market)^2 * (b_d + b_s) / 2，需代入具体市场弹性系数计算数值。

## Corrected Claim

基准工作点（B2）：当前均衡下的 Deadweight Loss (DWL) 量化公式 DWL = ∫_{P_market}^{P_ask} (D(P) - S(P)) dP，在假设 D(P) 和 S(P) 为线性函数且斜率分别为 -b_d 和 b_s 的简化模型下，DWL 可解析为 (P_ask - P_market)^2 * (b_d + b_s) / 2，需代入具体市场弹性系数计算数值。

## Evidence

先验知识/题面给定，逻辑校验通过：线性供需模型下DWL公式推导正确，量纲与数值逻辑自洽
