# N54: 卖家策略集 S_s 的量化：price 策略空间为 [intrinsic_value * 0.8, intrinsic_value * 1.5]，reduce_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

卖家策略集 S_s 的量化：price 策略空间为 [intrinsic_value * 0.8, intrinsic_value * 1.5]，reduce_price_timing 策略空间为 {T1=24h, T2=48h, T3=7d}；卖家选择概率由效用梯度 ∇U_seller 决定，初始时选择 price=intrinsic_value*1.2 的概率最高（≈60%）。

## Corrected Claim

卖家策略集 S_s 的量化：price 策略空间为 [intrinsic_value * 0.8, intrinsic_value * 1.5]，reduce_price_timing 策略空间为 {T1=24h, T2=48h, T3=7d}；卖家选择概率由效用梯度 ∇U_seller 决定，初始时选择 price=intrinsic_value*1.2 的概率最高（≈60%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller pricing strategy space probability distribution second hand platform
