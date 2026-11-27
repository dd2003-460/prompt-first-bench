# N132: P(negative_signal) 的贝叶斯更新公式：P(negative_signal) = P(defect | price_drop) = [P(pri

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

P(negative_signal) 的贝叶斯更新公式：P(negative_signal) = P(defect | price_drop) = [P(price_drop | defect) * P(defect)] / [P(price_drop | defect) * P(defect) + P(price_drop | no_defect) * (1 - P(defect))], 其中 P(defect) 为先验缺陷概率，P(price_drop | defect) 和 P(price_drop | no_defect) 为似然比，需通过历史成交数据估计 P(defect) 和似然比。

## Corrected Claim

P(negative_signal) 的贝叶斯更新公式：P(negative_signal) = P(defect | price_drop) = [P(price_drop | defect) * P(defect)] / [P(price_drop | defect) * P(defect) + P(price_drop | no_defect) * (1 - P(defect))], 其中 P(defect) 为先验缺陷概率，P(price_drop | defect) 和 P(price_drop | no_defect) 为似然比，需通过历史成交数据估计 P(defect) 和似然比。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式严格符合贝叶斯定理推导，量纲与逻辑自洽。

## Search Query

Bayes theorem defect probability price drop likelihood ratio historical data
