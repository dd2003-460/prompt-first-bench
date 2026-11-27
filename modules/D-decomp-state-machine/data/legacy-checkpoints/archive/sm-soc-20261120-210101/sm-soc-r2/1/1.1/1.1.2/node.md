# N31: 损失厌恶基线参数 λ_loss 的量化校准：基于 Kahneman & Tversky (1979) 前景理论，λ_loss = E[Loss] / E[Gai

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N6

## Claim

损失厌恶基线参数 λ_loss 的量化校准：基于 Kahneman & Tversky (1979) 前景理论，λ_loss = E[Loss] / E[Gain]。在二手交易语境下，需区分‘未成交损失’与‘价格偏离损失’的λ值差异，假设 λ_seller_unsold = 2.2, λ_buyer_overpay = 1.8，需通过实验数据验证。

## Corrected Claim

损失厌恶基线参数 λ_loss 的量化校准：基于 Kahneman & Tversky (1979) 前景理论，λ_loss 通常取值在 2-2.5 之间。在二手交易语境下，需区分‘未成交损失’与‘价格偏离损失’的λ值差异，具体数值（如 λ_seller_unsold 和 λ_buyer_overpay）需通过实验数据验证，而非直接假定为 2.2 和 1.8。

## Evidence

[质询]陈述中给出的具体数值（λ_seller_unsold = 2.2, λ_buyer_overpay = 1.8）缺乏明确的实证来源支持，且将前景理论中通常作为固定参数（约2-2.5）的λ值细分为不同交易角色的特定数值，属于未经证实的经验假设，而非理论推导结果。 | source=knowledge，逻辑自洽（前景理论框架下区分不同损失类型是合理的建模思路），但具体数值2.2和1.8属于经验事实，虽无来源直接矛盾，但也无来源直接支持，且检索无可用来源，故降级为定性表述。
