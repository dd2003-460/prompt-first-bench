# N305: vLLM 在 ROCm 6.0+ 环境下对 AMD Radeon PRO W7900 的 FP8 内核支持状态：截至 vLLM 0.5.x 版本，ROCm 后端

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103, N104, N105

## Claim

vLLM 在 ROCm 6.0+ 环境下对 AMD Radeon PRO W7900 的 FP8 内核支持状态：截至 vLLM 0.5.x 版本，ROCm 后端主要支持 BF16/FP16，FP8 量化内核（如 cutlass_fp8）尚未完全移植，需回退至 INT8 或 BF16，导致 W7900 在 FP8 场景下不可用。

## Corrected Claim

截至 vLLM 0.5.x 版本，ROCm 后端对 AMD Radeon PRO W7900 的 FP8 量化内核支持可能尚不完善，具体可用性需查阅该版本官方文档或社区 Issue 确认，通常建议回退至 INT8 或 BF16 以确保稳定性。

## Evidence

[质询]该陈述属于具体的软件版本兼容性经验事实（vLLM 0.5.x 在 ROCm 6.0+ 对 W7900 的 FP8 支持状态），无法从第一性原理推导，且检索无可用来源支持，存在版本迭代或特定配置下已支持 FP8 的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM ROCm 6.0 FP8 kernel support AMD Radeon PRO W7900 status
