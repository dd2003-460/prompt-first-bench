# N207: 边界条件：λ_loss 在极端损失情境下的非线性修正，量化为 λ_loss_effective = λ_base * (1 + γ * (L_loss / L_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

边界条件：λ_loss 在极端损失情境下的非线性修正，量化为 λ_loss_effective = λ_base * (1 + γ * (L_loss / L_max)^2)，当损失幅度 L_loss 超过市场均价的 50% 时，γ ≈ 0.5 导致 λ_loss_effective 显著偏离 2.0-2.5 的线性预测，需验证二手商品是否触发此非线性阈值。

## Corrected Claim

边界条件：λ_loss 在极端损失情境下存在非线性修正机制，量化形式为 λ_loss_effective = λ_base * (1 + γ * (L_loss / L_max)^2)。当损失幅度 L_loss 超过市场均价的 50% 时，非线性项显著，导致 λ_loss_effective 偏离线性预测值。具体参数 γ 及阈值需根据特定市场数据校准，此处假设 γ ≈ 0.5 作为示例。

## Evidence

[质询]该陈述包含具体的经验参数（γ ≈ 0.5, 阈值 50%, 线性预测区间 2.0-2.5），这些并非第一性原理可推导的数学或物理常数，而是特定模型或经验拟合的结果。作为 knowledge 节点，虽然逻辑结构自洽，但缺乏外部来源验证其具体数值参数的准确性，存在参数设定任意性的风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值参数（γ, 阈值）属于经验事实，无来源支持，故降级。

## Search Query

non-linear loss aversion extreme loss threshold secondary market
