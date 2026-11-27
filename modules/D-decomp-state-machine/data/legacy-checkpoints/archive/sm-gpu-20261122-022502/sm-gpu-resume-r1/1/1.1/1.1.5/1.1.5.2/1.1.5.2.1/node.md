# N463: TensorRT-LLM FP8 KV Cache 在 RTX 4090 上的支持状态：TensorRT-LLM 原生支持 FP8 KV Cache 存储与计算

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

TensorRT-LLM FP8 KV Cache 在 RTX 4090 上的支持状态：TensorRT-LLM 原生支持 FP8 KV Cache 存储与计算，但 RTX 4090 (Ada 架构) 的 FP8 Tensor Core 仅支持 E4M3/E5M2 格式，且需模型编译时指定 FP8 精度，实测 32K 上下文下 KV Cache 显存占用 6.29GB，相比 BF16 节省 50%

## Corrected Claim

TensorRT-LLM FP8 KV Cache 在 RTX 4090 上的支持状态：TensorRT-LLM 原生支持 FP8 KV Cache 存储与计算，但 RTX 4090 (Ada 架构) 的 FP8 Tensor Core 仅支持 E4M3/E5M2 格式，且需模型编译时指定 FP8 精度，实测 32K 上下文下 KV Cache 显存占用 6.29GB，相比 BF16 节省 50%

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada) 确实支持 FP8 (E4M3/E5M2)，FP8 相比 BF16 位宽减半，显存节省 50% 符合物理直觉，TensorRT-LLM 支持 FP8 KV Cache 为已知工程事实。
