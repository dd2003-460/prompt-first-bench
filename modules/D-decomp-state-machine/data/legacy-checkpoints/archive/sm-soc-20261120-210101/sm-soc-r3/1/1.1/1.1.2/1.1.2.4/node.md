# N127: 下游投影3：价格偏离损失厌恶 λ_price_dev 的量化，定义为 λ_price_dev = λ_seller_unsold * (1 + |D|/τ_si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N31

## Claim

下游投影3：价格偏离损失厌恶 λ_price_dev 的量化，定义为 λ_price_dev = λ_seller_unsold * (1 + |D|/τ_signal)，其中 D 为价格偏离度，τ_signal 为信号阈值（来自 N107，约15%），用于解释为何高溢价时卖家的‘不降价’倾向更强。

## Corrected Claim

下游投影3：价格偏离损失厌恶 λ_price_dev 的量化，定义为 λ_price_dev = λ_seller_unsold * (1 + |D|/τ_signal)，其中 D 为价格偏离度，τ_signal 为信号阈值（来自 N107，约15%），用于解释为何高溢价时卖家的‘不降价’倾向更强。

## Evidence

先验知识/题面给定，逻辑校验通过
