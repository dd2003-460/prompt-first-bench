# N396: AMD MI300X ROCm软件栈性能折损工作点2（缺乏TensorRT-LLM等效优化）：由于缺乏AMD等效的TensorRT-LLM高级编译优化（如Fla

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N141

## Claim

AMD MI300X ROCm软件栈性能折损工作点2（缺乏TensorRT-LLM等效优化）：由于缺乏AMD等效的TensorRT-LLM高级编译优化（如FlashAttention-2/3的特定HBM优化路径），在长上下文（32K）场景下，额外性能折损约为5-10%（相对于原生vLLM），累计总折损约为15-25%，即实际吞吐量仅为理论CUDA峰值的75-85%，此范围用于保守估计性价比上限。

## Corrected Claim

由于缺乏AMD等效的TensorRT-LLM高级编译优化，在长上下文场景下，AMD MI300X ROCm软件栈可能存在显著的性能折损，具体数值需参考最新基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性性能数据（5-10%额外折损、15-25%总折损、75-85%吞吐量），属于硬件/软件栈的具体性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AMD MI300X long context inference performance loss ROCm
