# N791: TCO 交叉点计算需引入折旧年限。若硬件折旧期为 3 年，则 Mac 的年均 CapEx 为 $6999/3 = $2333，2x 4090 为 $5198/3

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N246

## Claim

TCO 交叉点计算需引入折旧年限。若硬件折旧期为 3 年，则 Mac 的年均 CapEx 为 $6999/3 = $2333，2x 4090 为 $5198/3 = $1733。结合 OpEx，Mac 的年均 TCO = $2333 + $696 = $3029，2x 4090 = $1733 + $9198 = $10931。在此折旧模型下，Mac 方案在 3 年周期内 TCO 显著更低，原 0.29 年的交叉点结论失效。

## Corrected Claim

TCO 交叉点计算需引入折旧年限。若硬件折旧期为 3 年，则 Mac 的年均 CapEx 为 $6999/3 = $2333，2x 4090 为 $5198/3 = $1733。结合 OpEx，Mac 的年均 TCO = $2333 + $696 = $3029，2x 4090 = $1733 + $9198 = $10931。在此折旧模型下，Mac 方案在 3 年周期内 TCO 显著更低，原 0.29 年的交叉点结论失效。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（6999/3=2333, 5198/3=1733, 2333+696=3029, 1733+9198=10931），且基于3年折旧期的TCO对比逻辑自洽，结论符合经济直觉。

## Search Query

GPU depreciation schedule 3 years TCO calculation
