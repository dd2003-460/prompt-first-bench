# N134: 季节性混杂变量的量化：构建时间序列模型（如 SARIMA）拟合平台整体咨询量 $V_t$，提取季节项 $S_t$；需计算在 60% 无咨询样本所对应的时间窗口内

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

季节性混杂变量的量化：构建时间序列模型（如 SARIMA）拟合平台整体咨询量 $V_t$，提取季节项 $S_t$；需计算在 60% 无咨询样本所对应的时间窗口内，季节项 $S_t$ 是否处于全年最低分位（如 <10th percentile），若否，则排除季节性因素，归因于算法机制。

## Corrected Claim

季节性混杂变量的量化：构建时间序列模型（如 SARIMA）拟合平台整体咨询量 $V_t$，提取季节项 $S_t$；需计算在 60% 无咨询样本所对应的时间窗口内，季节项 $S_t$ 是否处于全年最低分位（如 <10th percentile），若否，则排除季节性因素，归因于算法机制。

## Evidence

先验知识/题面给定，逻辑校验通过
