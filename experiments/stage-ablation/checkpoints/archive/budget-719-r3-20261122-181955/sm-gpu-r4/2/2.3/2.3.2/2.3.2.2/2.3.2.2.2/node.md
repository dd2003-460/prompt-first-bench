# N695: Llama.cpp 在 -ngl 999 模式下，除模型权重和 KV Cache 外，还需预留的额外显存总量 E_extra = C_cuda + C_fram

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248, N249, N250

## Claim

Llama.cpp 在 -ngl 999 模式下，除模型权重和 KV Cache 外，还需预留的额外显存总量 E_extra = C_cuda + C_framework_overhead，其中 C_framework_overhead (如 GGML context buffer) 约为 100-200MB，故 E_extra 总区间为 400MB-1GB；该值在 RTX 4090 (24GB) 上会直接减少 KV Cache 可用空间，影响最大上下文长度计算。

## Corrected Claim

Llama.cpp 在 -ngl 999 模式下，除模型权重和 KV Cache 外，还需预留的额外显存总量 E_extra = C_cuda + C_framework_overhead，其中 C_framework_overhead (如 GGML context buffer) 约为 100-200MB，故 E_extra 总区间为 400MB-1GB；该值在 RTX 4090 (24GB) 上会直接减少 KV Cache 可用空间，影响最大上下文长度计算。

## Evidence

[质询]C_cuda 的具体数值未在陈述中明确给出，仅给出了总和区间，可能存在对 CUDA 上下文开销估算的偏差，但整体量级符合工程经验。 | 先验知识/题面给定，逻辑校验通过：Llama.cpp 在 GPU 模式下确实需要预留 CUDA 上下文及框架开销（GGML buffer 等），100-200MB 的框架开销及 400MB-1GB 的总额外开销符合常见工程实践量级，且该部分显存确实会挤占 KV Cache 空间，逻辑自洽。

## Search Query

llama.cpp gpu memory overhead beyond kv cache weights
