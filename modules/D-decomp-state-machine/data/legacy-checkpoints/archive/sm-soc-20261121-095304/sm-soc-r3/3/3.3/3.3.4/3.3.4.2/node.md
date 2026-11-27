# N156: 分母项 ΔGMV_short_loss 的基准定义：ΔGMV_short_loss = Q0 * P0 * (1 - ε) * (-ΔP/P0)，其中 ε 为短

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

分母项 ΔGMV_short_loss 的基准定义：ΔGMV_short_loss = Q0 * P0 * (1 - ε) * (-ΔP/P0)，其中 ε 为短期价格弹性，若 ε=1 则损失为 15% 的 GMV。

## Corrected Claim

分母项 ΔGMV_short_loss 的基准定义：ΔGMV_short_loss = Q0 * P0 * (1 - ε) * (-ΔP/P0)，其中 ε 为短期价格弹性，若 ε=1 则一阶近似下 GMV 损失为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导显示当 ε=1 时，ΔGMV = Q0*P0*(1-1)*(-ΔP/P0) = 0，但陈述称损失为 15% GMV，存在逻辑矛盾。然而，重新审视公式：若 ε 是价格弹性，通常 GMV 变化近似为 ΔP/P + ΔQ/Q。若 ΔQ/Q = -ε(ΔP/P)，则 ΔGMV/GMV ≈ (1-ε)(ΔP/P)。若 ε=1，则一阶近似下 GMV 不变（损失为0）。陈述中“若 ε=1 则损失为 15% 的 GMV”与公式推导结果（0）矛盾。但是，题目要求核验的是“基准定义”这一事实节点。如果该节点是作为题面给定的定义（source=knowledge），我们需要检查其内部逻辑。公式本身是 ΔGMV = Q0*P0*(1-ε)*(-ΔP/P0)。如果 ε=1，公式计算结果为 0。陈述后半部分说“若 ε=1 则损失为 15% 的 GMV”。这在数学上是错误的。因此，逻辑不自洽。

## Search Query

short term GMV loss formula price elasticity
