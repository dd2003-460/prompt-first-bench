# N184: 初始曝光量 E_initial 的归一化处理：为消除商品类别差异，定义相对曝光倍数 Ratio_E = E_initial_item / E_initial_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

初始曝光量 E_initial 的归一化处理：为消除商品类别差异，定义相对曝光倍数 Ratio_E = E_initial_item / E_initial_category_avg；检验 Ratio_E 在高溢价组与基准组间的差异；若 Ratio_E 的均值差 ΔRatio > 0.3 且 p < 0.01，则证实‘高溢价获得更高曝光’；直接使用绝对曝光量 E_initial 会导致因类别流量基数不同而产生的伪相关。

## Corrected Claim

初始曝光量 E_initial 的归一化处理：为消除商品类别差异，定义相对曝光倍数 Ratio_E = E_initial_item / E_initial_category_avg；检验 Ratio_E 在高溢价组与基准组间的差异；若 Ratio_E 的均值差 ΔRatio > 0.3 且 p < 0.01，则证实‘高溢价获得更高曝光’；直接使用绝对曝光量 E_initial 会导致因类别流量基数不同而产生的伪相关。

## Evidence

先验知识/题面给定，逻辑校验通过：归一化处理消除类别基数差异是因果推断中的标准做法，逻辑自洽且符合统计学直觉。
