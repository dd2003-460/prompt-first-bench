# N279: vLLM FP8 GEMM 算子在 Ada (RTX 4090) 上的实测加速比：基于 vLLM 官方 benchmark 或社区实测数据，计算 FP8 相比 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

vLLM FP8 GEMM 算子在 Ada (RTX 4090) 上的实测加速比：基于 vLLM 官方 benchmark 或社区实测数据，计算 FP8 相比 BF16 的 Tokens/s 提升系数；理论加速比 1.5x-2x 需修正为实际值，考虑 GEMM 形状（非方阵）对 Tensor Core 利用率的折损，预期实测加速比约为 1.3x-1.6x [待核验]。

## Corrected Claim

vLLM FP8 GEMM 算子在 Ada (RTX 4090) 上的实测加速比通常低于理论峰值，受 GEMM 形状影响，预期实测加速比约为 1.3x-1.6x（具体数值需依据最新 vLLM 官方 benchmark 或社区实测数据确认）。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1.3x-1.6x），属于硬件性能实测数据，无法从第一性原理严格推导，且缺乏来源支持以确认该特定范围在 vLLM 官方或社区实测中的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM FP8 benchmark RTX 4090 Ada tensor core speedup ratio vs BF16
