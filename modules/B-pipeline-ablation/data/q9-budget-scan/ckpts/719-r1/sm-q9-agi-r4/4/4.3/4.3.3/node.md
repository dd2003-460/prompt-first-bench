# N65: 误差容忍度 < 0.1% 的量化定义：对于数值型输出（如浮点数结果），相对误差 E_rel = |X_calc - X_ref| / |X_ref| < 0.0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

误差容忍度 < 0.1% 的量化定义：对于数值型输出（如浮点数结果），相对误差 E_rel = |X_calc - X_ref| / |X_ref| < 0.001；对于分类型输出（如标签），错误率 E_cat = (Mismatched Labels) / Total Labels < 0.001。需明确 X_ref 的来源（如高精度 CPU 计算或解析解）。

## Corrected Claim

误差容忍度 < 0.1% 的量化定义：对于数值型输出（如浮点数结果），相对误差 E_rel = |X_calc - X_ref| / |X_ref| < 0.001；对于分类型输出（如标签），错误率 E_cat = (Mismatched Labels) / Total Labels < 0.001。需明确 X_ref 的来源（如高精度 CPU 计算或解析解）。

## Evidence

先验知识/题面给定，逻辑校验通过
