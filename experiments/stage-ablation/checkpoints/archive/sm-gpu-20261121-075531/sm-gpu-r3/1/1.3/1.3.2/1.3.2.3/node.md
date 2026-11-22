# N150: vLLM 框架在初始化 PagedAttention 块表及 CUDA Graph 捕获时的额外固定显存开销约为 200-400MB，高于原生 PyTorch 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

vLLM 框架在初始化 PagedAttention 块表及 CUDA Graph 捕获时的额外固定显存开销约为 200-400MB，高于原生 PyTorch 推理，主要源于预分配的 KV Cache 块池（即使未完全使用）。

## Corrected Claim

vLLM 框架在初始化 PagedAttention 块表及 CUDA Graph 捕获时会产生额外的固定显存开销，该开销高于原生 PyTorch 推理，主要源于预分配的 KV Cache 块池；具体数值（如 200-400MB）取决于模型规模、最大序列长度及块大小等配置参数。

## Evidence

[质询]数值量级缺乏通用性：200-400MB 的固定开销高度依赖于模型架构（如层数、头数）、序列长度上限及块大小配置，并非 vLLM 框架的固有常数；对于小型模型或短序列配置，该开销可能显著低于此范围，对于大型模型则可能更高。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为依赖具体配置的工程经验值，非第一性原理可推导）

## Search Query

vLLM fixed memory overhead PagedAttention initialization GPU
