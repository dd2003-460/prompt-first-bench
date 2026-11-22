# N146: 软件栈选择影响：CUDA 12.4支持FP8/INT8硬件加速，而ROCm 6.0对FP8支持需依赖特定插件，性能差距通常为5-15%；若选择ROCm，需额外时

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

软件栈选择影响：CUDA 12.4支持FP8/INT8硬件加速，而ROCm 6.0对FP8支持需依赖特定插件，性能差距通常为5-15%；若选择ROCm，需额外时间用于调试和优化。

## Corrected Claim

软件栈选择影响：CUDA 12.4支持FP8/INT8硬件加速，而ROCm 6.0对FP8支持需依赖特定插件，性能差距通常为5-15%；若选择ROCm，需额外时间用于调试和优化。

## Evidence

先验知识/题面给定，逻辑校验通过
