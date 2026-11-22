# N212: GPTQ 量化模型在 TensorRT-LLM 中未进行 Kernel 融合优化时，具体的吞吐量下降 15-20% 源于：GEMM 算子无法利用 Tensor 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

GPTQ 量化模型在 TensorRT-LLM 中未进行 Kernel 融合优化时，具体的吞吐量下降 15-20% 源于：GEMM 算子无法利用 Tensor Core 的 INT8 加速路径，需回退到 CUDA Core 或进行动态反量化，导致每 token 计算延迟增加 [待核验] ms。

## Corrected Claim

GPTQ 量化模型在 TensorRT-LLM 中未进行 Kernel 融合优化时，由于 GEMM 算子无法直接利用 Tensor Core 的 INT8 加速路径，需回退到 CUDA Core 或进行动态反量化，导致每 token 计算延迟增加，吞吐量显著下降（具体幅度依硬件和模型而异，通常可达 15-20% 或更高）。

## Evidence

[质询]具体数值（15-20% 吞吐量下降、[待核验] ms 延迟增加）属于经验事实，缺乏来源支持，且不同硬件/模型规模下差异巨大，无法从第一性原理严格推出具体数值。 | 逻辑自洽（GPTQ 非原生 TensorRT-LLM 格式，需反量化或低效 Kernel，确实导致性能损失），但具体数值为经验事实，检索无可用来源，依据经验事实排除条款降级。

## Search Query

TensorRT-LLM GPTQ kernel fusion overhead latency penalty INT8
