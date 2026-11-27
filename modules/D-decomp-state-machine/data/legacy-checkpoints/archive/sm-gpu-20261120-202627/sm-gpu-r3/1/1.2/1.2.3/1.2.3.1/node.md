# N175: INT8/FP8 精度下权重显存占用及总需求计算：若权重也量化为 INT8 (1 byte/param)，权重占用 = 27 GB。总显存需求 = 权重 (27

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

INT8/FP8 精度下权重显存占用及总需求计算：若权重也量化为 INT8 (1 byte/param)，权重占用 = 27 GB。总显存需求 = 权重 (27 GB) + KV Cache (1.4 GB) + 激活值/框架开销 (估计 1-2 GB) ≈ 29.4-30.4 GB。此数值表明单张 RTX 4090 (24GB) 仍不足以运行 INT8 权重的 Qwen3-27B，必须使用 2× RTX 4090 (48GB) 或单张 A100/H100 (80GB+)，从而确定了最小可行硬件配置边界。

## Corrected Claim

INT8/FP8 精度下权重显存占用及总需求计算：若权重也量化为 INT8 (1 byte/param)，权重占用 = 27 GB。总显存需求 = 权重 (27 GB) + KV Cache (1.4 GB) + 激活值/框架开销 (估计 1-2 GB) ≈ 29.4-30.4 GB。此数值表明单张 RTX 4090 (24GB) 仍不足以运行 INT8 权重的 Qwen3-27B，必须使用 2× RTX 4090 (48GB) 或单张 A100/H100 (80GB+)，从而确定了最小可行硬件配置边界。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数×1Byte=27GB权重，加上KV Cache和激活值开销，总显存需求约30GB，超过单张RTX 4090 (24GB)容量，需双卡或80GB+单卡，推导自洽。

## Search Query

Qwen3-27B INT8 quantized memory requirement single GPU
