# N9: 非典型方案纳入判据：纳入Apple Silicon Mac Studio (M2/M3 Ultra, 192GB+统一内存) 和 AMD Instinct MI

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

非典型方案纳入判据：纳入Apple Silicon Mac Studio (M2/M3 Ultra, 192GB+统一内存) 和 AMD Instinct MI300X，仅当其单位吞吐成本（$/token）低于NVIDIA同级方案15%以上时保留，否则标记为[排除]，因为其软件栈优化（MLX/ROCm）对Qwen3-27B的算子支持度需单独验证。

## Corrected Claim

非典型方案纳入判据：纳入Apple Silicon Mac Studio (M2/M3 Ultra, 192GB+统一内存) 和 AMD Instinct MI300X，仅当其单位吞吐成本（$/token）低于NVIDIA同级方案15%以上时保留，否则标记为[排除]，因为其软件栈优化（MLX/ROCm）对Qwen3-27B的算子支持度需单独验证。

## Evidence

先验知识/题面给定，逻辑校验通过
