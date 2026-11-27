# N308: Activation_Peak 精度依赖修正：N129 中假设 Activation 固定为 2.5GB。实际上 Activation 精度通常跟随权重精度或独

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

Activation_Peak 精度依赖修正：N129 中假设 Activation 固定为 2.5GB。实际上 Activation 精度通常跟随权重精度或独立设置。若权重为 INT8/NVFP4，Activation 可量化为 INT8/FP8，占用减半。例如，BF16 Activation 2.5GB -> FP8 Activation 1.25GB。需根据所选精度重新计算 Activation 项，而非使用固定值。

## Corrected Claim

Activation_Peak 精度依赖修正：N129 中假设 Activation 固定为 2.5GB。实际上 Activation 精度通常跟随权重精度或独立设置。若权重为 INT8/NVFP4，Activation 可量化为 INT8/FP8，占用减半。例如，BF16 Activation 2.5GB -> FP8 Activation 1.25GB。需根据所选精度重新计算 Activation 项，而非使用固定值。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8 精度为 8 位，BF16 为 16 位，数据量减半符合基本算术逻辑（2.5GB / 2 = 1.25GB），且符合深度学习量化常识。
