# N53: RTX 3090 (二手) 的 BF16 理论峰值算力为 35.6 TFLOPS，FP8 支持有限（无原生 Tensor Core 加速，需软件模拟或仅 INT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

RTX 3090 (二手) 的 BF16 理论峰值算力为 35.6 TFLOPS，FP8 支持有限（无原生 Tensor Core 加速，需软件模拟或仅 INT8），显存 24GB 同样仅支持 W4/INT8 低精度推理，其单位算力价格低于 RTX 4090 但能效比更低。

## Corrected Claim

RTX 3090 (二手) 的 BF16 理论峰值算力为 35.6 TFLOPS，FP8 支持有限（无原生 Tensor Core 加速，需软件模拟或仅 INT8），显存 24GB 同样仅支持 W4/INT8 低精度推理，其单位算力价格低于 RTX 4090 但能效比更低。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 (GA102) 的 BF16 Tensor Core 峰值算力确为 35.6 TFLOPS (73.2 TFLOPS FP16 / 2)，且 Ampere 架构不支持原生 FP8 Tensor Core 加速，需软件模拟或回退至 INT8/FP16，显存 24GB 及能效比描述符合硬件规格事实。
