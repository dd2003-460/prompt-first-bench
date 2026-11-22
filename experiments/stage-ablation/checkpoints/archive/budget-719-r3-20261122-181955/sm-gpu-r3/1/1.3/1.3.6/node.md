# N57: ROCm 5.7+ 支持 Qwen3-27B 的 FP16/BF16 推理，但 INT8/INT4 量化支持较 NVIDIA CUDA 滞后，性能损失约 10-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

ROCm 5.7+ 支持 Qwen3-27B 的 FP16/BF16 推理，但 INT8/INT4 量化支持较 NVIDIA CUDA 滞后，性能损失约 10-20% [待核验]

## Corrected Claim

ROCm 5.7+ 支持 Qwen3-27B 的 FP16/BF16 推理，并支持多种量化格式（如 FP8、GGUF），但关于 INT8/INT4 量化相对于 NVIDIA CUDA 的具体性能损失比例（10-20%）缺乏直接数据支持，需进一步实测验证。

## Evidence

[质询]陈述中关于“INT8/INT4 量化支持较 NVIDIA CUDA 滞后”及“性能损失约 10-20%”的具体量化指标和对比结论缺乏直接证据支持，且参考来源主要涉及 FP8 或 GGUF 量化，未直接提供 INT8/INT4 在 ROCm 5.7+ 上的具体性能对比数据。 | 来源 [1] 和 [2] 证实了 ROCm 环境支持 Qwen3 系列 27B 模型的推理（包括 FP8 和 GGUF 量化），间接支持了基础推理能力的存在，但均未提供 INT8/INT4 量化相对于 CUDA 的具体性能损失数据（10-20%），属于经验事实且缺乏直接来源支持。

## Search Query

ROCm support Qwen3-27B FP16 BF16 INT8 performance benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32495691/article/details/163809701&rut=57d7003bb34a5d0b46c588a51b200c6afd408d3e19b5f65c399aa348283b52bb', 'type': 'ddg', 'title': 'AMD GPU本地部署Qwen3.8-27B：从ROCm到OpenCL的完整实践指南-CSDN博客'}
- {'url': 'https://www.modelscope.cn/posts/434795&rut=ff99b725f31d8217104eebc80a20a6031a92e268b13aaec126397f1ab8cbc8fd', 'type': 'ddg', 'title': '在AMD ROCm上部署Qwen3.6-27B-FP8：vLLM推理与服务实践'}
