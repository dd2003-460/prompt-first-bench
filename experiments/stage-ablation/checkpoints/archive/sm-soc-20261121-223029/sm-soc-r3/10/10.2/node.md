# N122: 高溢价商品在前24小时的曝光量增量ΔImpression：对比δ>20%组与δ<10%组的平均曝光次数，预期高溢价组曝光量高出20-40%，需排除商品本身质量或

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

高溢价商品在前24小时的曝光量增量ΔImpression：对比δ>20%组与δ<10%组的平均曝光次数，预期高溢价组曝光量高出20-40%，需排除商品本身质量或图片质量混杂变量后，通过回归系数β_exposure量化溢价对曝光的净影响。

## Corrected Claim

高溢价商品在前24小时的曝光量增量ΔImpression：对比δ>20%组与δ<10%组的平均曝光次数，预期高溢价组曝光量显著高于低溢价组，需排除商品本身质量或图片质量混杂变量后，通过回归系数β_exposure量化溢价对曝光的净影响。

## Evidence

父节点级核验未通过：不完备（子节点正交性良好，分别处理变量定义、核心回归和敏感性检验。但完备性不足：父节点明确要求“对比δ>20%组与δ<10%组”并预期“高出20-40%”，这属于非参数或半参数的描述性统计/分箱分析，而子节点仅提供了全样本的连续变量OLS回归，缺失了针对特定溢价区间的分组对比分析及基准效应量验证。）

## Search Query

impact of high asking price on initial 24-hour impressions second-hand platform A/B test data
