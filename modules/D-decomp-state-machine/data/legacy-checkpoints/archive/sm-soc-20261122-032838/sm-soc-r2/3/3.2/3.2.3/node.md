# N69: 平台福利变化 $\Delta U_p$ 取决于佣金模式。若为固定比例佣金 $\epsilon$，$\Delta U_p = \epsilon \Delta GM

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

平台福利变化 $\Delta U_p$ 取决于佣金模式。若为固定比例佣金 $\epsilon$，$\Delta U_p = \epsilon \Delta GMV$。$\Delta GMV$ 由价格下降带来的交易量增加 $\Delta Q$ 和单价下降 $\Delta P$ 共同决定：$\Delta GMV = Q \Delta P + P \Delta Q + \Delta P \Delta Q$。若需求价格弹性 $E_d = -1.5$，价格下降10%导致销量增加15%，则 $\Delta GMV = -10\% + 15\% - 1.5\% = +3.5\%$，平台受益。若 $E_d < -1$（富有弹性），平台受益；若 $E_d > -1$（缺乏弹性），平台受损。二手市场非标准化商品通常 $|E_d| > 1$，故平台短期可能受益。

## Corrected Claim

平台福利变化 $\Delta U_p$ 取决于佣金模式。若为固定比例佣金 $\epsilon$，$\Delta U_p = \epsilon \Delta GMV$。$\Delta GMV$ 由价格下降带来的交易量增加 $\Delta Q$ 和单价下降 $\Delta P$ 共同决定：$\Delta GMV = Q \Delta P + P \Delta Q + \Delta P \Delta Q$。若需求价格弹性 $E_d = -1.5$，价格下降10%导致销量增加15%，则 $\Delta GMV = -10\% + 15\% - 1.5\% = +3.5\%$，平台受益。若 $E_d < -1$（富有弹性），平台受益；若 $E_d > -1$（缺乏弹性），平台受损。二手市场非标准化商品通常 $|E_d| > 1$，故平台短期可能受益。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV变化公式推导正确，弹性与GMV变动关系符合经济学原理，数值计算无误

## Search Query

platform GMV impact of price transparency demand elasticity second hand market commission revenue
