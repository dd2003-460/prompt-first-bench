# N15: 总显存需求 = 权重显存 + KV Cache显存 + 激活值缓冲(~2-5 GB) + CUDA上下文(~1-2 GB)。BF16: 54 + 4.29 + 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

总显存需求 = 权重显存 + KV Cache显存 + 激活值缓冲(~2-5 GB) + CUDA上下文(~1-2 GB)。BF16: 54 + 4.29 + 3.5 ≈ 61.8 GB；FP8: 27 + 2.15 + 3.5 ≈ 32.65 GB；INT8: 27 + 2.15 + 3.5 ≈ 32.65 GB；NVFP4: 13.5 + 1.07 + 3.5 ≈ 18.07 GB；W4: 13.5 + 1.07 + 3.5 ≈ 18.07 GB

## Corrected Claim

总显存需求 = 权重显存 + KV Cache显存 + 激活值缓冲(~2-5 GB) + CUDA上下文(~1-2 GB)。BF16: 54 + 4.29 + 3.5 ≈ 61.8 GB；FP8: 27 + 2.15 + 3.5 ≈ 32.65 GB；INT8: 27 + 2.15 + 3.5 ≈ 32.65 GB；NVFP4: 13.5 + 1.07 + 3.5 ≈ 18.07 GB；W4: 13.5 + 1.07 + 3.5 ≈ 18.07 GB

## Evidence

先验知识/题面给定，逻辑校验通过：显存构成公式符合LLM推理显存估算标准模型，各精度下的权重与KV Cache数值量级及加法运算结果均自洽。

## Search Query

LLM inference total VRAM requirement weights KV cache activation buffer CUDA context
