# N298: 允许误差 E 的设定依据：E 通常设定为置信区间宽度的半宽，如 E = 0.05 * P_median（即价格中位数的 5%）；若 E 越小，所需样本量 N_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

允许误差 E 的设定依据：E 通常设定为置信区间宽度的半宽，如 E = 0.05 * P_median（即价格中位数的 5%）；若 E 越小，所需样本量 N_obs 按 1/E² 增长，需根据业务容忍度确定具体数值

## Corrected Claim

允许误差 E 的设定依据：E 通常设定为置信区间宽度的半宽，如 E = 0.05 * P_median（即价格中位数的 5%）；若 E 越小，所需样本量 N_obs 按 1/E² 增长，需根据业务容忍度确定具体数值

## Evidence

先验知识/题面给定，逻辑校验通过：样本量公式 N ∝ 1/E² 符合统计学基本原理，E 设定为相对误差（如 5%）是常见业务实践。
