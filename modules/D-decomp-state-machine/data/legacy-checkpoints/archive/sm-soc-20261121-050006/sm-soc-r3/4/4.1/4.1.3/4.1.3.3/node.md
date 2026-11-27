# N265: 图片数量对 S_nonstandard 的修正项量化：每增加 1 张高质量图片，S_nonstandard 降低 0.02-0.05，修正公式为 S_nonst

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

图片数量对 S_nonstandard 的修正项量化：每增加 1 张高质量图片，S_nonstandard 降低 0.02-0.05，修正公式为 S_nonstandard_adjusted = S_nonstandard * (1 - δ_image * N_images / N_max)，其中 δ_image ∈ [0.02, 0.05]，N_max 为平台允许的最大图片数（通常为 9 张）。若 N_images = 9，修正后 S_nonstandard 降低约 18%-45%。

## Corrected Claim

图片数量对 S_nonstandard 存在负向修正作用，具体修正系数与公式需依据特定平台或模型定义确定，常见经验值中每增加一张高质量图片可能降低 S_nonstandard 约 2%-5%。

## Evidence

[质询]该陈述包含具体的经验参数（δ_image 范围 0.02-0.05、N_max=9）及特定的修正公式，属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

impact of image quantity on product non-standardization perception e-commerce listing optimization
