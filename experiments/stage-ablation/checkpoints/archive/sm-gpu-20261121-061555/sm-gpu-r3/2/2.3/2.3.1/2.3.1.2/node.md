# N189: TensorRT-LLM 的 CUDA Context 及算子库（如 FlashInfer, CUTLASS）预加载导致的固定显存开销，通常比 vLLM 高约 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

TensorRT-LLM 的 CUDA Context 及算子库（如 FlashInfer, CUTLASS）预加载导致的固定显存开销，通常比 vLLM 高约 0.2-0.4 GB，具体值取决于编译时包含的算子数量及引擎序列化文件大小。

## Corrected Claim

TensorRT-LLM 的 CUDA Context 及算子库（如 FlashInfer, CUTLASS）预加载导致的固定显存开销，通常比 vLLM 高约 0.2-0.4 GB，具体值取决于编译时包含的算子数量及引擎序列化文件大小。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TensorRT-LLM CUDA context memory overhead vs vLLM
