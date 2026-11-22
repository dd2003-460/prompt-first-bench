# N292: 置信度衰减的数学形式：C_hypothesis = P(H_best | Data) ≈ exp(-ΔAIC / 2)，其中 ΔAIC 为最佳模型与次优模型之差

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

置信度衰减的数学形式：C_hypothesis = P(H_best | Data) ≈ exp(-ΔAIC / 2)，其中 ΔAIC 为最佳模型与次优模型之差；若 ΔAIC > 10，则次优假设置信度衰减至 <0.5%，视为被排除

## Corrected Claim

置信度衰减的数学形式：C_hypothesis = P(H_best | Data) ≈ exp(-ΔAIC / 2)，其中 ΔAIC 为最佳模型与次优模型之差；若 ΔAIC > 10，则次优假设置信度衰减至 <0.5%，视为被排除

## Evidence

先验知识/题面给定，逻辑校验通过：AIC 差值与后验概率近似关系符合贝叶斯信息准则推导，ΔAIC>10 对应似然比约 22000:1，次优模型后验概率确实极低（<0.5%），数值量级与逻辑自洽。
