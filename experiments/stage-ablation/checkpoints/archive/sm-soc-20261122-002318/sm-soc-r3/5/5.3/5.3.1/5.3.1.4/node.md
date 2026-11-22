# N231: β_speed/β_price 置信区间的计算方法：基于回归系数的标准误 SE_β，利用误差传播定律或Delta Method计算比值 R = β_speed/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

β_speed/β_price 置信区间的计算方法：基于回归系数的标准误 SE_β，利用误差传播定律或Delta Method计算比值 R = β_speed/β_price 的近似标准误 SE_R ≈ sqrt((SE_speed/β_price)^2 + (β_speed*SE_price/β_price^2)^2)，进而构建 95% CI = R ± 1.96 * SE_R。

## Corrected Claim

β_speed/β_price 置信区间的计算方法：基于回归系数的标准误 SE_β，利用误差传播定律或Delta Method计算比值 R = β_speed/β_price 的近似标准误 SE_R ≈ sqrt((SE_speed/β_price)^2 + (β_speed*SE_price/β_price^2)^2)，进而构建 95% CI = R ± 1.96 * SE_R。

## Evidence

先验知识/题面给定，逻辑校验通过
