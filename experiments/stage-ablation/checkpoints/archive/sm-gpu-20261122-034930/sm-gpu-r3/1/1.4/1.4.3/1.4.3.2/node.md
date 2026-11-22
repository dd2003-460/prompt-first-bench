# N186: 主流推理框架（如llama.cpp, vLLM with GPTQ/AWQ）在W4权重下默认强制使用FP16 KV Cache，因为INT8 KV Cache与

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

主流推理框架（如llama.cpp, vLLM with GPTQ/AWQ）在W4权重下默认强制使用FP16 KV Cache，因为INT8 KV Cache与W4权重的组合会导致显著的精度损失（>5% MMLU drop）且缺乏硬件加速支持，因此W4方案的总显存需求应按FP16 KV Cache计算，即13.5GB (W4) + 10.7GB (FP16 KV) + 4GB (Framework) = 28.2GB，与N19一致。

## Corrected Claim

主流推理框架在W4权重下通常推荐使用FP16 KV Cache以保证精度，但部分框架也支持INT8 KV Cache以节省显存；若按FP16 KV Cache计算，总显存需求约为28.2GB。

## Evidence

[质询]陈述中关于“默认强制使用FP16 KV Cache”以及“INT8 KV Cache与W4权重组合导致>5% MMLU drop”的具体数值和默认行为属于经验事实，且不同框架（如vLLM）实际上支持并广泛使用INT8/FP8 KV Cache以节省显存，并非“强制”FP16，该绝对化表述存在事实偏差。 | 经验事实，逻辑自洽但缺来源支持；且“强制FP16”与主流框架实际支持低精度KV Cache的现状存在潜在矛盾，故降级。

## Search Query

W4 quantization FP16 KV cache default framework requirement llama.cpp vLLM
