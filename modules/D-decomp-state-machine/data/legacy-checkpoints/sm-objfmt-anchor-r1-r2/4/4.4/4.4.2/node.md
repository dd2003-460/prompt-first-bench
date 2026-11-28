# N89: NVFP4 精度下的质量损失量化：NVFP4 (4-bit floating point with block-wise scaling) 是较新的量化方案，理

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

NVFP4 精度下的质量损失量化：NVFP4 (4-bit floating point with block-wise scaling) 是较新的量化方案，理论上比 INT4 更好地保留动态范围；预计 ΔPPL 介于 INT4 和 FP8 之间 (0.05-0.15)，但目前缺乏大规模第三方评测，主要参考 NVIDIA TensorRT-LLM 官方示例数据 [待核验: 需查找 H100/H200 上 NVFP4 的公开基准]。

## Corrected Claim

NVFP4 (4-bit floating point with block-wise scaling) 理论上比 INT4 更好地保留动态范围，其质量损失（ΔPPL）预计介于 INT4 和 FP8 之间。目前缺乏大规模第三方评测，具体数值范围（如 0.05-0.15）主要参考 NVIDIA TensorRT-LLM 官方示例数据，尚需在 H100/H200 等硬件上进行公开基准验证。

## Evidence

[质询]该陈述包含具体的经验数值范围（ΔPPL 0.05-0.15）和特定硬件上的性能预期，属于经验事实而非第一性原理可推导内容；且明确指出‘缺乏大规模第三方评测’，主要依赖官方示例，存在以偏概全或特定场景过拟合的风险。 | 经验事实，逻辑自洽（4-bit浮点通常优于INT4且劣于FP8的定性逻辑成立），但缺来源支持（本轮检索无可用来源，且原陈述自述缺乏大规模第三方评测）。

## Search Query

TensorRT-LLM NVFP4 quantization accuracy benchmark Llama Qwen
