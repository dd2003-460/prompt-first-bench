# N538: RTX 5090 单卡 FP8 实际性能与理论值的偏差来源：除带宽外，Tensor Core 利用率在 FP8 推理中受限于算子融合效率，vLLM/Tensor

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N222

## Claim

RTX 5090 单卡 FP8 实际性能与理论值的偏差来源：除带宽外，Tensor Core 利用率在 FP8 推理中受限于算子融合效率，vLLM/TensorRT-LLM 在 Blackwell 架构上的优化程度 (截至 2025 年中) 可能使实际 MFU 低于 50%，导致吞吐量比纯带宽估算低 20-30%，需结合具体推理引擎版本实测数据 [待核验]。

## Corrected Claim

RTX 5090 单卡 FP8 实际性能与理论值的偏差受 Tensor Core 利用率及算子融合效率影响，vLLM/TensorRT-LLM 在 Blackwell 架构上的优化程度可能导致实际 MFU 低于理论峰值，具体吞吐量偏差需结合特定推理引擎版本及模型配置实测数据确定。

## Evidence

[质询]具体数值（MFU < 50%, 吞吐量低 20-30%）缺乏公开基准测试支持，且不同推理引擎（vLLM vs TensorRT-LLM）及模型规模下差异巨大，该量化结论可能过于绝对或基于特定未披露场景。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能偏差数值属于经验参数，无法从第一性原理严格推出）

## Search Query

RTX 5090 FP8 inference benchmark vLLM TensorRT-LLM tokens per second
