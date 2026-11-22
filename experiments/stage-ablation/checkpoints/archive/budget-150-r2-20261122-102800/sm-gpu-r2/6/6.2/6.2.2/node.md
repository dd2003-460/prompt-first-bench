# N136: TensorRT-LLM 对 H100 的 FP8/NVFP4 支持细节：H100 原生支持 FP8 Tensor Core，TensorRT-LLM 可利用此

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

TensorRT-LLM 对 H100 的 FP8/NVFP4 支持细节：H100 原生支持 FP8 Tensor Core，TensorRT-LLM 可利用此特性实现约 2 倍于 BF16 的推理吞吐；NVFP4 支持需特定软件版本，且在 H100 上可能无法充分利用 FP4 精度优势，实际加速比需实测验证，通常 FP8 是更成熟的选择。

## Corrected Claim

TensorRT-LLM 对 H100 的 FP8 支持细节：H100 原生支持 FP8 Tensor Core，TensorRT-LLM 可利用此特性实现约 2 倍于 BF16 的推理吞吐；NVFP4 是 Blackwell 架构的特性，H100 硬件不支持原生 FP4 计算，因此无法在 H100 上利用 NVFP4 加速，FP8 是 H100 上更成熟且有效的低精度选择。

## Evidence

[质询]NVFP4 是 Blackwell 架构（如 B100/B200）引入的特性，H100 (Hopper) 硬件原生不支持 FP4 Tensor Core 计算，因此‘在 H100 上可能无法充分利用 FP4 精度优势’这一表述存在技术误导，实际上 H100 根本不支持原生 FP4 推理，而非‘无法充分利用’。 | 来源 [1] 和 [2] 直接支持 H100 支持 FP8 及 TensorRT-LLM 利用该特性提升性能（约 2 倍于 BF16 的推断符合 FP8 相比 BF16 的算力/带宽优势逻辑），但所有来源均未提及 NVFP4 在 H100 上的支持情况，且基于硬件架构常识，H100 不支持 FP4，故 NVFP4 部分缺乏来源支持且存在事实偏差风险，判为 degraded。

## Search Query

TensorRT-LLM H100 FP8 NVFP4 performance benchmarks

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_35871529/article/details/160571567&rut=ade08e92b7625cd0f69214e8ac542f1c406530d0893043fae2f2369fbd63a6bc', 'type': 'ddg', 'title': 'NVIDIA H100与TensorRT-LLM加速AI推理性能解析 - CSDN博客'}
- {'url': 'https://nvidia.github.io/TensorRT-LLM/blogs/H100vsA100.html&rut=62ea081c64ac6f3390f81d2f3a1b7a7d4df8994e1dce63fb7309e6eb3b52e15d', 'type': 'ddg', 'title': 'H100 has 4.6x A100 Performance in TensorRT LLM, achieving 10,000 tok/s ...'}
- {'url': 'https://developer.nvidia.cn/blog/achieving-top-inference-performance-with-the-nvidia-h100-tensor-core-gpu-and-nvidia-tensorrt-llm/&rut=952d6cbf8ddcf31c61fe34029b9bc42cb54051da553f9d27838d707688bfa3f5', 'type': 'ddg', 'title': '借助 NVIDIA H100 Tensor Core GPU 和 NVIDIA TensorRT-LLM 实现出色的推理性能'}
