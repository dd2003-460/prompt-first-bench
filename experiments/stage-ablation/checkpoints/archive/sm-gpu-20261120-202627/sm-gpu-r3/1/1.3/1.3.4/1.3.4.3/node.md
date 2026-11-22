# N187: NVFP4 运行时开销量化：包括激活值缓冲、CUDA 上下文及 vLLM/TensorRT-LLM 框架内存分配，通常估算为 5-8 GB，具体取决于 Batc

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

NVFP4 运行时开销量化：包括激活值缓冲、CUDA 上下文及 vLLM/TensorRT-LLM 框架内存分配，通常估算为 5-8 GB，具体取决于 Batch Size 和框架版本。

## Corrected Claim

NVFP4 运行时开销包括激活值缓冲、CUDA 上下文及框架内存分配，其具体数值高度依赖于 Batch Size、模型规模及框架版本，通常需根据实际部署配置进行动态估算，而非固定为 5-8 GB。

## Evidence

[质询]数值量级缺乏普适性：5-8 GB 的固定估算范围对于不同 Batch Size 和模型规模而言过于僵化，未区分具体硬件配置（如 H100 vs A100）及模型参数量，可能导致在大规模推理场景下严重低估或在小规模场景下高估开销。 | 先验知识/题面给定，逻辑校验通过，但具体数值范围属于经验事实且缺乏来源直接支持，故降级为定性表述。
