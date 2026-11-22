# N280: vLLM FP8 GEMM 算子在 Blackwell (RTX 5090) 上的实测加速比：基于 CUDA 12.8+ 驱动及 PyTorch 2.4+ 环境

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

vLLM FP8 GEMM 算子在 Blackwell (RTX 5090) 上的实测加速比：基于 CUDA 12.8+ 驱动及 PyTorch 2.4+ 环境下的实测数据，计算 FP8 相比 BF16 的 Tokens/s 提升系数；Blackwell 架构的 FP8 Tensor Core 吞吐量理论提升需结合内存带宽瓶颈进行修正，预期实测加速比约为 1.4x-1.8x [待核验]。

## Corrected Claim

vLLM FP8 GEMM 算子在 Blackwell (RTX 5090) 上相比 BF16 具有显著加速潜力，具体加速比取决于内存带宽瓶颈及实现细节，通常预期在 1.4x-1.8x 范围内，但需以实际基准测试为准。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1.4x-1.8x）和特定硬件/软件版本依赖（RTX 5090, CUDA 12.8+, PyTorch 2.4+），属于无法从第一性原理严格推导的经验事实。由于缺乏实测数据或权威基准测试来源支持，且不同实现（如 vLLM 具体版本、量化方案）可能导致显著差异，该具体数值范围缺乏实证依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体加速比数值）

## Search Query

vLLM FP8 benchmark RTX 5090 Blackwell tensor core speedup ratio vs BF16
