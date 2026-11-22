# N11: 软件栈兼容性矩阵：NVIDIA 消费级卡（RTX 4090/5090）支持 BF16/FP8 (需 CUDA 12.8+ 及新驱动)，但原生不支持 NVFP4；

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

软件栈兼容性矩阵：NVIDIA 消费级卡（RTX 4090/5090）支持 BF16/FP8 (需 CUDA 12.8+ 及新驱动)，但原生不支持 NVFP4；数据中心卡（A100/H100/B200）全面支持 BF16/FP8/NVFP4/INT8；AMD 卡（MI300X/MI325X）支持 BF16/FP8，但对 INT8/W4 的支持依赖 ROCm 版本，存在 [时效待核] 风险。

## Corrected Claim

软件栈兼容性矩阵：NVIDIA 数据中心卡（A100/H100/B200）全面支持 BF16/FP8/NVFP4/INT8；消费级卡（RTX 4090/5090）支持 BF16/FP8，NVFP4 支持需依赖特定 CUDA/驱动版本及软件栈更新；AMD 卡（MI300X/MI325X）支持 BF16/FP8，INT8/W4 支持依赖 ROCm 版本。

## Evidence

[质询]参考来源仅提供了NVIDIA框架支持矩阵的通用描述，未包含具体硬件型号（RTX 4090/5090, A100等）对特定精度（BF16/FP8/NVFP4/INT8）的支持细节，无法直接验证陈述中的具体兼容性断言。 | 逻辑自洽（符合当前硬件架构常识：Hopper/Blackwell支持FP8/NVFP4，Ada/Blackwell消费级支持FP8但NVFP4支持情况需具体驱动/软件栈确认，AMD ROCm支持情况随版本变化），但参考来源[1]仅为主题相关，未提供具体数值或型号支持，属于间接支持或缺乏直接证据。

## Search Query

NVIDIA RTX 4090 FP8 support CUDA version Qwen3 inference framework compatibility vLLM llama.cpp

## Retrieval Sources

- {'url': 'https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html&rut=1ab62f78f369c3b092afa13cd0b700062c986d8fcfbd7fb8b411c78cb882c4a5', 'type': 'ddg', 'title': 'Frameworks Support Matrix - NVIDIA Docs'}
