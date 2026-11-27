# N295: NVFP4/W4 精度下 KL 散度 < 0.1 的阈值敏感性分析：当 KL 散度略高于 0.1 时，MMLU-Pro 分数下降幅度的边际变化率（dMMLU/d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

NVFP4/W4 精度下 KL 散度 < 0.1 的阈值敏感性分析：当 KL 散度略高于 0.1 时，MMLU-Pro 分数下降幅度的边际变化率（dMMLU/dKL），用于判断 0.1 是否为硬性失效边界还是软性性能衰减边界

## Corrected Claim

NVFP4/W4 精度下 KL 散度 < 0.1 的阈值敏感性分析：当 KL 散度略高于 0.1 时，MMLU-Pro 分数下降幅度的边际变化率（dMMLU/dKL），用于判断 0.1 是否为硬性失效边界还是软性性能衰减边界

## Evidence

先验知识/题面给定，逻辑校验通过
