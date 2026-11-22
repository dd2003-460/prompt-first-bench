# N195: RTX 4090 不支持原生 FP8 硬件加速，其 FP8 推理吞吐量提升（1.8-2.1x）主要源于软件栈（如 TensorRT-LLM 或 vLLM）的算子

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

RTX 4090 不支持原生 FP8 硬件加速，其 FP8 推理吞吐量提升（1.8-2.1x）主要源于软件栈（如 TensorRT-LLM 或 vLLM）的算子优化与内存访问模式改进，而非硬件 FP8 单元；需验证该提升是否依赖于特定 CUDA 版本（如 CUDA 12.6+）和 cuDNN 版本，不同版本间吞吐量差异可达 10-15%。

## Corrected Claim

RTX 4090 支持原生 FP8 硬件加速（通过 Tensor Core），其 FP8 推理吞吐量相比 FP16 有显著提升（官方标称 1.3 PFLOPS）；软件栈（如 TensorRT-LLM）的优化可进一步挖掘硬件潜力，但基础加速能力源于硬件支持。

## Evidence

[质询]陈述声称RTX 4090不支持原生FP8硬件加速，但参考来源[1]明确引用NVIDIA官方数据指出RTX 4090提供1.3 PetaFLOPS的FP8 AI推理性能，且FP8相比FP16吞吐量翻倍，这直接证明了其具备原生FP8硬件加速能力（通过Tensor Core支持）。 | 来源[1]直接矛盾：NVIDIA官方确认RTX 4090支持FP8计算并给出具体性能指标（1.3 PFLOPS），反驳了'不支持原生FP8硬件加速'的核心论断。

## Search Query

RTX 4090 FP8 inference throughput improvement TensorRT-LLM CUDA version dependency

## Retrieval Sources

- {'url': 'https://forums.developer.nvidia.com/t/4090-doesnt-have-fp8-compute/232256&rut=ffc21d5edbe17735e6be9fac0ca3daa28aafa49aa7be2e6fb70ad9a3d0909e38', 'type': 'ddg', 'title': "4090 doesn't have fp8 compute? - NVIDIA Developer Forums"}
