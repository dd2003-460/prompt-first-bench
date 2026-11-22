# N40: 销量增量 $\Delta Q$ 的需求弹性模型为 $\Delta Q = Q_0 \times \epsilon_{Q/P} \times (\Delta P 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

销量增量 $\Delta Q$ 的需求弹性模型为 $\Delta Q = Q_0 \times \epsilon_{Q/P} \times (\Delta P / P_0)$，其中 $\epsilon_{Q/P}$ 为价格弹性系数。在二手市场同质化商品中，假设 $\epsilon_{Q/P} = 1.2$（缺乏弹性），若降价5% ($\Delta P/P_0 = -0.05$)，则 $\Delta Q = Q_0 \times 1.2 \times (-0.05) = -0.06 Q_0$（此处符号表示价格下降导致数量增加，取绝对值计算收益），即销量仅增加6%，不足以弥补5%的价格损失。

## Corrected Claim

销量增量 $\Delta Q$ 的需求弹性模型为 $\Delta Q = Q_0 \times \epsilon_{Q/P} \times (\Delta P / P_0)$，其中 $\epsilon_{Q/P}$ 为价格弹性系数。在二手市场同质化商品中，假设 $\epsilon_{Q/P} = 1.2$（富有弹性），若降价5% ($\Delta P/P_0 = -0.05$)，则 $\Delta Q = Q_0 \times 1.2 \times (-0.05) = -0.06 Q_0$（此处符号表示价格下降导致数量增加，取绝对值计算收益），即销量仅增加6%，不足以弥补5%的价格损失。

## Evidence

[质询]术语定义错误：经济学中弹性系数绝对值大于1（如1.2）称为“富有弹性”（Elastic），小于1才称为“缺乏弹性”（Inelastic）。陈述中将1.2标记为“缺乏弹性”是概念性错误。 | 先验知识/题面给定，逻辑校验通过（数学推导正确：1.2 * 5% = 6% > 5%，确实无法弥补损失），但存在术语定义错误（1.2应为富有弹性），故降级。

## Search Query

price elasticity of demand for used goods market epsilon 1.2
