# N331: FP8 KV Cache的硬件兼容性约束：在RTX 4090 (Ada) 上，FP8 KV Cache需依赖Tensor Core的FP8支持，但Attenti

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

FP8 KV Cache的硬件兼容性约束：在RTX 4090 (Ada) 上，FP8 KV Cache需依赖Tensor Core的FP8支持，但Attention Kernel（如FlashAttention-2/3）需显式启用FP8路径；若框架（vLLM/SGLang）未针对GQA结构优化FP8 KV Cache内核，实际吞吐量提升可能低于理论值（显存带宽减半带来的2x加速），实测提升通常在1.2x-1.5x之间 [待核验]，因为GQA的KV头数少（8 heads）导致矩阵乘法形状不规则，FP8 GEMM效率降低。

## Corrected Claim

FP8 KV Cache在RTX 4090上需依赖Tensor Core FP8支持及Kernel显式启用；由于GQA结构及Kernel优化程度影响，实际吞吐量提升通常低于理论2x加速，具体提升幅度取决于框架实现与硬件适配情况。

## Evidence

[质询]具体数值区间（1.2x-1.5x）和特定硬件行为（GQA导致FP8 GEMM效率降低的具体幅度）属于经验事实，缺乏直接来源支持，且不同框架/版本实测数据可能存在差异，无法仅凭逻辑推导确定精确范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM FP8 KV cache GQA performance boost RTX 4090 benchmark
