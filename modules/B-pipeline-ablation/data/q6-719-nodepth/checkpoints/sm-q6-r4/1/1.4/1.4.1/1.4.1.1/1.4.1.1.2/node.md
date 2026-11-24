# N522: 平均单张图片大小 s_img 的分布特征：假设均值为2MB，但实际服从对数正态分布，P95大小约为5-10MB，需考虑压缩算法（WebP/AVIF）对大小的影响

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N175

## Claim

平均单张图片大小 s_img 的分布特征：假设均值为2MB，但实际服从对数正态分布，P95大小约为5-10MB，需考虑压缩算法（WebP/AVIF）对大小的影响，修正后的有效均值 s_img_eff = 2MB × Compression_Factor (0.5-0.8)

## Corrected Claim

平均单张图片大小 s_img 的分布特征：假设均值为2MB，但实际服从对数正态分布，P95大小约为5-10MB，需考虑压缩算法（WebP/AVIF）对大小的影响，修正后的有效均值 s_img_eff = 2MB × Compression_Factor (0.5-0.8)

## Evidence

先验知识/题面给定，逻辑校验通过：图片大小服从对数正态分布符合经验规律，P95为均值2.5-5倍合理，压缩因子0.5-0.8符合WebP/AVIF典型性能，数值量级自洽。

## Search Query

average image file size web upload MB distribution log-normal
