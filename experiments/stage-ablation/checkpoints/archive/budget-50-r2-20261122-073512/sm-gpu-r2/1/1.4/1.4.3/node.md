# N52: 框架与 CUDA 上下文开销项量化：Overhead_GB = 2.0 (基准) + 0.1 × N_gpus (多卡通信缓冲) + 0.5 (TensorRT

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

框架与 CUDA 上下文开销项量化：Overhead_GB = 2.0 (基准) + 0.1 × N_gpus (多卡通信缓冲) + 0.5 (TensorRT/vLLM 编译缓存)，该值在单卡 BF16 下约为 2.5 GB，多卡下随 GPU 数量线性增加。

## Corrected Claim

框架与 CUDA 上下文开销项量化：Overhead_GB ≈ 2.0 (基准) + 0.1 × N_gpus (多卡通信缓冲) + 0.5 (编译缓存)，该值为典型经验估算，单卡 BF16 下约为 2.5 GB，多卡下随 GPU 数量线性增加，具体数值依框架版本和配置而异。

## Evidence

[质询]具体数值（2.0GB基准、0.1GB/卡、0.5GB缓存）属于经验性工程估算，缺乏通用标准，不同框架版本、模型规模及驱动配置下差异巨大，无法作为普适事实。 | 先验知识/题面给定，逻辑校验通过（量纲正确，线性增长符合多卡通信缓冲直觉），但具体数值为经验估算，无来源直接支持，故降级。
