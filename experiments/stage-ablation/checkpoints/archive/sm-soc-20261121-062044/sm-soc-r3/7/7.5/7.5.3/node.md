# N261: 重复曝光伪相关校正系数 k_dup 的计算：k_dup = 1 + (Total_Impressions / Unique_Users - 1) * β_rep

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

重复曝光伪相关校正系数 k_dup 的计算：k_dup = 1 + (Total_Impressions / Unique_Users - 1) * β_repeat，其中 β_repeat 为重复曝光对咨询概率的边际衰减系数（通常 0.1-0.3），若 k_dup > 1.5，则必须使用 Unique_Users 作为分母以消除高活跃用户带来的方差膨胀。

## Corrected Claim

重复曝光伪相关校正系数 k_dup 的计算：k_dup = 1 + (Total_Impressions / Unique_Users - 1) * β_repeat，其中 β_repeat 为重复曝光对咨询概率的边际衰减系数（通常 0.1-0.3），若 k_dup > 1.5，则必须使用 Unique_Users 作为分母以消除高活跃用户带来的方差膨胀。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

correcting for repeat exposure bias in CTR and inquiry rate calculation
