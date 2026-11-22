# N141: INT8 权重 + FP8 KV Cache 方案中，基础开销（2.03GB）的具体构成：包括 CUDA Context、cuBLAS Workspaces、以

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

INT8 权重 + FP8 KV Cache 方案中，基础开销（2.03GB）的具体构成：包括 CUDA Context、cuBLAS Workspaces、以及框架元数据（如 PagedAttention 块表），需量化各部分占比，以判断在显存紧张时（如 48GB 卡）是否有优化空间（如减少 Workspace 大小）

## Corrected Claim

INT8 权重 + FP8 KV Cache 方案中，基础开销（如 CUDA Context、cuBLAS Workspaces、PagedAttention 块表等）的具体数值因框架版本、GPU 型号及配置而异（例如在特定配置下可能约为 2.03GB），需量化各部分占比以评估在显存紧张时的优化空间。

## Evidence

[质询]该陈述包含具体的经验数值（2.03GB）和特定的组件构成比例，属于经验事实。由于缺乏外部来源支持，无法验证该具体数值在特定硬件/软件版本下的准确性，且不同框架（如 vLLM, TensorRT-LLM）的开销构成差异巨大，直接断言具体数值存在风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。CUDA Context、cuBLAS Workspace 和 PagedAttention 元数据确实是显存开销的主要组成部分，但具体数值 2.03GB 无法通过第一性原理推导，需依赖具体环境实测。

## Search Query

llama.cpp vLLM base memory overhead CUDA context cuBLAS workspace size
