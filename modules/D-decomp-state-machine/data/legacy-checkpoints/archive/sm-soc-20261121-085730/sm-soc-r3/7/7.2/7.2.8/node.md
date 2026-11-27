# N384: 好评率 R_good 的计算需剔除异常评价：R_good = (N_positive_reviews - N_suspicious) / (N_total_re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133, N134, N135

## Claim

好评率 R_good 的计算需剔除异常评价：R_good = (N_positive_reviews - N_suspicious) / (N_total_reviews - N_suspicious)，其中 N_suspicious 为被平台风控标记的疑似刷单或恶意差评数量，若 N_total_reviews - N_suspicious < 5，则不满足‘高好评率’条件。

## Corrected Claim

好评率 R_good 的计算需剔除异常评价：R_good = (N_positive_reviews - N_suspicious) / (N_total_reviews - N_suspicious)，其中 N_suspicious 为被平台风控标记的疑似刷单或恶意差评数量，若 N_total_reviews - N_suspicious < 5，则不满足‘高好评率’条件。

## Evidence

先验知识/题面给定，逻辑校验通过
