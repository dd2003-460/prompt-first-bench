# N223: 双重差分（DID）平行趋势检验：计算干预前各期处理组与对照组结果变量（如曝光量或成交量）的均值差序列 D_t，进行 Hausman-Taylor 或简单的联合 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

双重差分（DID）平行趋势检验：计算干预前各期处理组与对照组结果变量（如曝光量或成交量）的均值差序列 D_t，进行 Hausman-Taylor 或简单的联合 F 检验（H0: D_t = 0 for all t < T0），若 p > 0.05 则平行趋势假设成立，DID 估计量 β_DID = (Y_treat,post - Y_treat,pre) - (Y_ctrl,post - Y_ctrl,pre) 无偏。

## Corrected Claim

双重差分（DID）平行趋势检验：计算干预前各期处理组与对照组结果变量（如曝光量或成交量）的均值差序列 D_t，进行 Hausman-Taylor 或简单的联合 F 检验（H0: D_t = 0 for all t < T0），若 p > 0.05 则平行趋势假设成立，DID 估计量 β_DID = (Y_treat,post - Y_treat,pre) - (Y_ctrl,post - Y_ctrl,pre) 无偏。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DID parallel trends test Hausman-Taylor specification
