# N96: BF16 权重显存占用的 54GB 仅包含模型参数本身，未包含推理框架 (如 vLLM, TensorRT-LLM) 的运行时开销 (Runtime Overh

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

BF16 权重显存占用的 54GB 仅包含模型参数本身，未包含推理框架 (如 vLLM, TensorRT-LLM) 的运行时开销 (Runtime Overhead)，通常额外占用 1-2GB 显存用于 CUDA 上下文、内核缓存及管理结构，实际可用显存需求应为 55-56GB。

## Corrected Claim

BF16 权重显存占用的 54GB 仅包含模型参数本身，未包含推理框架 (如 vLLM, TensorRT-LLM) 的运行时开销 (Runtime Overhead)，通常额外占用 1-2GB 显存用于 CUDA 上下文、内核缓存及管理结构，实际可用显存需求应为 55-56GB。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下54GB参数占用符合大模型量级，CUDA上下文及内核缓存等运行时开销通常在1-2GB范围内，总需求55-56GB符合工程常识。

## Search Query

vLLM TensorRT-LLM runtime memory overhead CUDA context size
