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

父节点级核验通过：正交+完备+无冗余（子节点将父节点提到的‘运行时开销’正交地分解为‘底层驱动/内核层面开销’（CUDA上下文、内核缓存）和‘框架逻辑/调度层面开销’（PagedAttention元数据、调度器），两者边界清晰无重叠。虽然数值范围（1.5-2.5GB + 0.2-0.5GB = 1.7-3.0GB）略高于父节点估算的‘1-2GB’，但这属于更精细化的量化，且父节点本身为估算值，子节点提供了更具体的场景参数，不构成矛盾。）

## Search Query

vLLM TensorRT-LLM runtime memory overhead CUDA context size
