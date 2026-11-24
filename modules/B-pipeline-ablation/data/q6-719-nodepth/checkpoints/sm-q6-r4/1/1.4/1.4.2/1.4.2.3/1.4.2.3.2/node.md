# N535: 对象大小 s_avg 的敏感性分析：若 R_per_user = 20 且 Hit_Rate = 99%，则 s_avg_inferred = Origin_T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N180

## Claim

对象大小 s_avg 的敏感性分析：若 R_per_user = 20 且 Hit_Rate = 99%，则 s_avg_inferred = Origin_Traffic / (R_total × (1 - Hit_Rate)) = 2048GB / (100,000,000 × 0.01) = 2.048MB；若 s_avg 确认为 3.6MB，则 Hit_Rate_inferred = 1 - 2048 / (100,000,000 × 3.6 / 1024) ≈ 99.44%；需确定 s_avg 是包含视频分片（chunk）还是完整文件，视频分片通常 500KB-2MB，完整短视频 5-20MB，此差异导致 Hit_Rate 估算偏差 > 10%。

## Corrected Claim

对象大小 s_avg 的敏感性分析：若 R_per_user = 20 且 Hit_Rate = 99%，则 s_avg_inferred = Origin_Traffic / (R_total × (1 - Hit_Rate)) = 2048GB / (100,000,000 × 0.01) = 2.048MB；若 s_avg 确认为 3.6MB，则 Hit_Rate_inferred = 1 - 2048 / (100,000,000 × 3.6 / 1024) ≈ 99.44%；需确定 s_avg 是包含视频分片（chunk）还是完整文件，视频分片通常 500KB-2MB，完整短视频 5-20MB，此差异导致 Hit_Rate 估算偏差 > 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（2048GB / 1,000,000 = 2.048MB；1 - 2048/(100,000,000 * 3.6 / 1024) ≈ 99.44%），且视频分片与完整文件的大小量级符合行业常识。

## Search Query

video CDN average object size chunk vs full file
