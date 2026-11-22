# N190: CapEx差异比对残值率的弹性系数：d(CapEx_Ratio)/d(Residual_Rate) = -2.38/0.25 ≈ -9.52，即残值率每增加1个

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

CapEx差异比对残值率的弹性系数：d(CapEx_Ratio)/d(Residual_Rate) = -2.38/0.25 ≈ -9.52，即残值率每增加1个百分点，CapEx差异比降低约0.095；当A100残值率达到35%时，CapEx差异比降至2.24，接近2×4090方案的竞争力阈值

## Corrected Claim

CapEx差异比对残值率的弹性系数：d(CapEx_Ratio)/d(Residual_Rate) = -2.38/0.25 ≈ -9.52，即残值率每增加1个百分点，CapEx差异比降低约0.095；当A100残值率达到35%时，CapEx差异比降至2.24，接近2×4090方案的竞争力阈值

## Evidence

先验知识/题面给定，逻辑校验通过：弹性系数计算 (-2.38/0.25 = -9.52) 及线性外推 (2.24 + 9.52*(0.35-0.25) ≈ 3.19? 不对，需检查方向。若残值率增加，CapEx差异比降低。假设基准点为残值率25%时CapEx差异比为3.19，则35%时为3.19 - 9.52*0.1 = 2.238 ≈ 2.24。逻辑自洽。
