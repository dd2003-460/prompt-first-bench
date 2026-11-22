# N124: FP8 量化的硬件-软件交互约束：FP8 量化必须配合支持 FP8 Tensor Core 的硬件 (如 RTX 4090 Ada, H100, B200) 才

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

FP8 量化的硬件-软件交互约束：FP8 量化必须配合支持 FP8 Tensor Core 的硬件 (如 RTX 4090 Ada, H100, B200) 才能发挥加速作用；若在仅支持 BF16/INT8 的旧硬件 (如 RTX 3090, A100) 上运行 FP8 权重，需反量化为 BF16 或 INT8，导致显存优势 (27GB) 失效且计算速度无增益，仅保留存储节省。

## Corrected Claim

FP8 量化的硬件-软件交互约束：FP8 量化必须配合支持 FP8 Tensor Core 的硬件 (如 RTX 4090 Ada, H100, B200) 才能发挥加速作用；若在仅支持 BF16/INT8 的旧硬件 (如 RTX 3090, A100) 上运行 FP8 权重，需反量化为 BF16 或 INT8，导致显存优势 (27GB) 失效且计算速度无增益，仅保留存储节省。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 加速依赖特定 Tensor Core 硬件支持，旧硬件需反量化导致计算无增益但保留存储优势，符合硬件架构原理。

## Search Query

FP8 quantization hardware support requirement Tensor Core RTX 4090 A100 dequantization overhead
