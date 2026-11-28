# N39: NVFP4 量化在 V100 (Compute Cap 7.0) 上运行时的内核支持情况：若 V100 不支持原生 FP4 Tensor Core 运算，vLL

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

NVFP4 量化在 V100 (Compute Cap 7.0) 上运行时的内核支持情况：若 V100 不支持原生 FP4 Tensor Core 运算，vLLM 将回退至 CPU 反量化或低效 GPU 模拟，导致实际推理吞吐低于理论值（需验证是否触发 Fallback 机制及性能惩罚系数）

## Corrected Claim

NVFP4 量化在 V100 (Compute Cap 7.0) 上运行时，由于硬件不支持原生 FP4 Tensor Core 运算，vLLM 将采用非原生路径（如反量化后使用 FP16/BF16 计算或 CPU 辅助），这通常会导致推理吞吐显著低于支持原生 FP4 的硬件（如 H100）的理论峰值，具体性能惩罚取决于实现细节。

## Evidence

[质询]该陈述包含具体的性能行为预测（'回退至CPU反量化或低效GPU模拟'、'吞吐低于理论值'），属于经验事实。V100 (CC 7.0) 确实不支持原生 FP4 Tensor Core（FP4 支持始于 Hopper/H100 CC 9.0），但 vLLM 的具体回退策略（是 CPU offload 还是 GPU 上的软件模拟/反量化）以及具体的性能惩罚系数是依赖特定版本实现的工程细节，无法从第一性原理严格推出，且缺乏来源支持。 | 经验事实，逻辑自洽（V100 硬件架构确实不支持 FP4 原生运算，必然导致非原生路径的性能损失），但缺来源支持具体回退机制和性能系数。

## Search Query

vLLM NVFP4 support on V100 compute capability 7.0 fallback performance
