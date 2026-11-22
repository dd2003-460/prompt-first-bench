# N111: 曝光率差异的统计显著性检验：计算Z统计量 $Z = \frac{E_{high} - E_{low}}{\sqrt{\frac{E_{high}(1-E_{hi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

曝光率差异的统计显著性检验：计算Z统计量 $Z = \frac{E_{high} - E_{low}}{\sqrt{\frac{E_{high}(1-E_{high})}{N_{high}} + \frac{E_{low}(1-E_{low})}{N_{low}}}}$，仅当 $|Z| > 1.96$ (p<0.05) 且效应量 Cohen's d > 0.2 时，才允许将置信度从0.6上调至0.9，否则维持原置信度。

## Corrected Claim

曝光率差异的统计显著性检验：计算Z统计量 $Z = \frac{E_{high} - E_{low}}{\sqrt{\frac{E_{high}(1-E_{high})}{N_{high}} + \frac{E_{low}(1-E_{low})}{N_{low}}}}$，仅当 $|Z| > 1.96$ (p<0.05) 且效应量 Cohen's d > 0.2 时，才允许将置信度从0.6上调至0.9，否则维持原置信度。

## Evidence

先验知识/题面给定，逻辑校验通过：Z统计量公式符合双比例检验标准，阈值1.96对应p<0.05，Cohen's d>0.2为小效应量标准，逻辑自洽且无矛盾。
