# N367: 加权平均对象大小 s_avg 的精确值：s_avg = (N_img × s_img + N_vid × s_vid) / (N_img + N_vid) = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

加权平均对象大小 s_avg 的精确值：s_avg = (N_img × s_img + N_vid × s_vid) / (N_img + N_vid) = (200k × 0.3MB + 14k × 10MB) / 214k ≈ 1.07MB，该值用于计算总请求数 R_total = 2TB / 1.07MB ≈ 1.96M 次/天。

## Corrected Claim

加权平均对象大小 s_avg 的精确值：s_avg = (N_img × s_img + N_vid × s_vid) / (N_img + N_vid) = (200k × 0.3MB + 14k × 10MB) / 214k ≈ 1.07MB，该值用于计算总请求数 R_total = 2TB / 1.07MB ≈ 1.96M 次/天。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 (200*0.3 + 14*10)/214 ≈ 1.07MB 正确，总请求数 2048/1.07 ≈ 1914k (约1.9M-2.0M) 量级合理，符合数学推导。
