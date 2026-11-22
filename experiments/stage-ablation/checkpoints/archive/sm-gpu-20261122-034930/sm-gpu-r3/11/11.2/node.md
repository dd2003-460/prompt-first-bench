# N424: NVFP4推理在RTX 4090 (Ada架构) 上无法原生支持，需回退至W4 INT4或FP8；回退至W4 INT4时，显存占用与NVFP4相近（~14GB）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N153

## Claim

NVFP4推理在RTX 4090 (Ada架构) 上无法原生支持，需回退至W4 INT4或FP8；回退至W4 INT4时，显存占用与NVFP4相近（~14GB），但推理速度降低约20-30%，因为Ada架构缺乏FP4专用Tensor Core，需通过软件模拟实现。

## Corrected Claim

NVFP4推理在RTX 4090 (Ada架构) 上无法原生支持，需回退至W4 INT4或FP8；回退至W4 INT4时，显存占用与NVFP4相近，但推理速度通常会因缺乏FP4专用硬件加速而有所降低，具体降幅取决于模型结构和软件实现。

## Evidence

[质询]该陈述包含具体的性能损耗数值（20-30%）和显存占用数值（~14GB），属于经验事实。由于缺乏外部来源支持，且不同模型规模、量化实现库（如TensorRT-LLM vs vLLM）及具体任务负载下，软件模拟FP4或回退INT4的性能差异波动极大，固定数值缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090 (Ada) 确实不支持原生FP4 Tensor Core（Blackwell特性），回退至INT4/FP8符合硬件架构逻辑，但具体性能损耗比例和显存数值无法从第一性原理严格推导，且无检索来源佐证。

## Search Query

NVIDIA Ada Lovelace FP4 support fallback W4 INT4 performance impact
