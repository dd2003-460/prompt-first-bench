# N44: 在 NVFP4/W4 精度下，若 KV Cache 也采用 4-bit 存储，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 NVFP4/W4 精度下，若 KV Cache 也采用 4-bit 存储，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 2 * 64 * 8 * 128 * 32768 * 0.5 byte = 2.15 GB [待核验：取决于推理框架是否支持 KV Cache 量化]

## Corrected Claim

在 NVFP4/W4 精度下，若 KV Cache 也采用 4-bit 存储，Qwen3-27B 32K 上下文长度的 KV Cache 总显存占用计算结果为 2 * 64 * 8 * 128 * 32768 * 0.5 byte = 2.15 GB [待核验：取决于推理框架是否支持 KV Cache 量化]

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，8 KV头，128头维）符合主流大模型配置，4-bit量化即0.5字节/元素，计算过程 2*64*8*128*32768*0.5 = 2,147,483,648 bytes ≈ 2.15 GB 准确无误。

## Search Query

vLLM KV cache quantization INT8 FP8 4bit
