# N445: A100 80GB PCIe 的 FP8 算力规格：A100 不支持原生 FP8 计算（FP8 为 Hopper 架构 H100 引入），A100 仅支持 BF

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151

## Claim

A100 80GB PCIe 的 FP8 算力规格：A100 不支持原生 FP8 计算（FP8 为 Hopper 架构 H100 引入），A100 仅支持 BF16/FP16/INT8/TF32，因此 N151 中 FP8 算力 624 TFLOPS 为错误前提，需修正为 INT8 或 BF16 等效对比。

## Corrected Claim

A100 80GB PCIe 的 FP8 算力规格：A100 不支持原生 FP8 计算（FP8 为 Hopper 架构 H100 引入），A100 仅支持 BF16/FP16/INT8/TF32，因此 N151 中 FP8 算力 624 TFLOPS 为错误前提，需修正为 INT8 或 BF16 等效对比。

## Evidence

先验知识/题面给定，逻辑校验通过：A100基于Ampere架构，确实不支持原生FP8（FP8为Hopper架构H100引入），仅支持BF16/FP16/INT8/TF32，因此原陈述中关于A100 FP8算力的前提错误，修正建议合理。

## Search Query

NVIDIA A100 FP8 support architecture
