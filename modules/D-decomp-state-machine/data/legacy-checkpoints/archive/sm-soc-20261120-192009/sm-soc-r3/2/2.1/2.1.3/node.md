# N55: 买家策略集 S_b 的量化：inspect 策略的概率 P(inspect) = 0.7（固定），wait 策略的概率 P(wait | price > P*)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

买家策略集 S_b 的量化：inspect 策略的概率 P(inspect) = 0.7（固定），wait 策略的概率 P(wait | price > P*) = 0.8，buy 策略的概率 P(buy | price < P*) = 0.9；买家策略选择受 info_quality 调节，info_quality 高时 P(wait) 降低 20%。

## Corrected Claim

买家策略集 S_b 的量化：inspect 策略的概率 P(inspect) = 0.7（固定），wait 策略的概率 P(wait | price > P*) = 0.8，buy 策略的概率 P(buy | price < P*) = 0.9；买家策略选择受 info_quality 调节，info_quality 高时 P(wait) 降低 20%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

buyer strategy selection probability inspect wait buy second hand market
