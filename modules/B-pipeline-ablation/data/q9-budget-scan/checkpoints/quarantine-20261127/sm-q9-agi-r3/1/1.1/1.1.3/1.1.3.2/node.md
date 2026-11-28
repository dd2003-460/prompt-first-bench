# N112: 工作点2（CUDA Context 精简/低开销）：通过禁用非必要 CUDA 特性（如 CUDA Graphs 若未启用则节省 ~0.5 GB/GPU）并优化 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

工作点2（CUDA Context 精简/低开销）：通过禁用非必要 CUDA 特性（如 CUDA Graphs 若未启用则节省 ~0.5 GB/GPU）并优化 cuBLAS Workspace 大小（设为 32 MB 而非默认 64-128 MB），可将 vLLM 运行时基础开销从 2.5 GB/GPU 降至 1.5-1.8 GB/GPU；总节省 4-8 GB 显存，可用于扩展 KV Cache 容量 10-15%。

## Corrected Claim

工作点2（CUDA Context 精简/低开销）：通过禁用非必要 CUDA 特性并优化 cuBLAS Workspace 大小，可降低 vLLM 运行时基础开销，从而释放显存用于扩展 KV Cache 容量。

## Evidence

[质询]具体数值（如0.5GB节省、32MB workspace、10-15% KV Cache提升）缺乏通用标准支持，高度依赖特定硬件、模型规模及vLLM版本配置，属于经验性调优数据而非固定常量。 | 先验知识/题面给定，逻辑校验通过（显存节省与KV Cache扩容的正相关关系符合直觉），但具体数值为经验事实且无外部来源直接支持，故降级。

## Search Query

vLLM CUDA context memory overhead reduction cuBLAS workspace size configuration
