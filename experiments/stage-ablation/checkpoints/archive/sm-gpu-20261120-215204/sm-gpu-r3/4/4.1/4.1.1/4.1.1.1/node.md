# N274: CUDA 上下文与内核缓存显存开销：在 vLLM 或 TensorRT-LLM 框架下，启动时预分配的内核缓存 (Kernel Cache) 和 CUDA 上下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

CUDA 上下文与内核缓存显存开销：在 vLLM 或 TensorRT-LLM 框架下，启动时预分配的内核缓存 (Kernel Cache) 和 CUDA 上下文通常占用 1.5GB - 2.5GB 显存，具体取决于加载的算子数量 (如 FlashAttention 版本、量化内核)，该部分不可被 KV Cache 动态复用。

## Corrected Claim

CUDA 上下文与内核缓存显存开销：在 vLLM 或 TensorRT-LLM 框架下，启动时预分配的内核缓存 (Kernel Cache) 和 CUDA 上下文通常占用 1.5GB - 2.5GB 显存，具体取决于加载的算子数量 (如 FlashAttention 版本、量化内核)，该部分不可被 KV Cache 动态复用。

## Evidence

先验知识/题面给定，逻辑校验通过
