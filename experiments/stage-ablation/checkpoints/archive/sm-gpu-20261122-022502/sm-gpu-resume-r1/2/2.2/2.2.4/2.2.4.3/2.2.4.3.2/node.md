# N601: ROCm 6.1 中 Flash Attention 2 在 MI300X 上的实测性能仅为 CUDA 版本的 85%，主要瓶颈在于 AMD CDNA3 架构对

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

ROCm 6.1 中 Flash Attention 2 在 MI300X 上的实测性能仅为 CUDA 版本的 85%，主要瓶颈在于 AMD CDNA3 架构对 Tensor Core 类似单元（MFMA）的指令调度延迟较高，且缺少针对 Attention 算子的专用硬件加速路径。

## Corrected Claim

ROCm 6.1 中 Flash Attention 2 在 MI300X 上的实测性能通常低于 CUDA 版本，主要瓶颈可能涉及 AMD CDNA3 架构的指令调度特性及软件优化程度，具体性能差距需依据特定测试环境确定。

## Evidence

[质询]该陈述包含具体的性能数值（85%）和特定的硬件瓶颈归因（指令调度延迟、缺少专用加速路径），属于经验事实。在缺乏外部来源支持的情况下，无法验证该具体数值及归因的准确性，且不同软件栈版本或优化程度下性能差异可能较大，存在口径混淆或数据过时的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Flash Attention 2 ROCm MI300X performance vs CUDA NVIDIA comparison
