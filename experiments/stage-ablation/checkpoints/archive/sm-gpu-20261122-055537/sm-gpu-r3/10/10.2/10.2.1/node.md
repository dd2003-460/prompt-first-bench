# N366: L4 上运行 FP8 模型的软件回退机制：当 vLLM 或 TensorRT-LLM 在 L4 上加载 FP8 权重时，框架必须将 FP8 权重反量化 (Deq

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115

## Claim

L4 上运行 FP8 模型的软件回退机制：当 vLLM 或 TensorRT-LLM 在 L4 上加载 FP8 权重时，框架必须将 FP8 权重反量化 (Dequantize) 为 FP16 或 BF16 进行矩阵乘法，或者转换为 INT8 进行计算。若反量化为 FP16，则显存占用恢复为 FP16 大小 (27GB)，且计算量与 FP16 相同，失去 FP8 的显存节省优势。

## Corrected Claim

L4 上运行 FP8 模型的软件回退机制：当 vLLM 或 TensorRT-LLM 在 L4 上加载 FP8 权重时，框架必须将 FP8 权重反量化 (Dequantize) 为 FP16 或 BF16 进行矩阵乘法，或者转换为 INT8 进行计算。若反量化为 FP16，则显存占用恢复为 FP16 大小 (27GB)，且计算量与 FP16 相同，失去 FP8 的显存节省优势。

## Evidence

先验知识/题面给定，逻辑校验通过：L4 (Turing架构) 硬件不支持原生FP8计算，软件回退至FP16/INT8是必然机制，且FP16显存占用恢复至27GB符合2x FP8的数学逻辑。

## Search Query

vLLM FP8 fallback on Ada Lovelace
