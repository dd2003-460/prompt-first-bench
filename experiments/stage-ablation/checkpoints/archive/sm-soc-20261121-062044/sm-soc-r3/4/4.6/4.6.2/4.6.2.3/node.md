# N236: 有限总体校正对标准误的具体修正公式：SE_corrected = SE_infinite * FPC，其中 SE_infinite = √(p(1-p)/n)；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

有限总体校正对标准误的具体修正公式：SE_corrected = SE_infinite * FPC，其中 SE_infinite = √(p(1-p)/n)；当 FPC < 0.8 时，若不应用修正，置信区间宽度将被高估 (1/FPC)^2 倍，导致保守估计掩盖真实显著性。

## Corrected Claim

有限总体校正对标准误的具体修正公式：SE_corrected = SE_infinite * FPC，其中 SE_infinite = √(p(1-p)/n)；当 FPC < 0.8 时，若不应用修正，置信区间宽度将被高估 (1/FPC)^2 倍，导致保守估计掩盖真实显著性。

## Evidence

先验知识/题面给定，逻辑校验通过
