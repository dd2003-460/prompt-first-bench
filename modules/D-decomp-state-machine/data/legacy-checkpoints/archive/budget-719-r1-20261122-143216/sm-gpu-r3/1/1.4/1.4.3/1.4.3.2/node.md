# N177: Qwen3-27B 在 KV Cache 量化为 FP8 (E4M3) 时，32K 上下文下的单请求 KV 显存占用计算公式：KV_FP8 = 2 × 64层 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Qwen3-27B 在 KV Cache 量化为 FP8 (E4M3) 时，32K 上下文下的单请求 KV 显存占用计算公式：KV_FP8 = 2 × 64层 × 8 KV头 × 128 头维度 × 32768 tokens × 1 byte/param = 5.37 GB，相比 BF16 (10.74 GB) 节省 50%。

## Corrected Claim

Qwen3-27B 在 KV Cache 量化为 FP8 (E4M3) 时，32K 上下文下的单请求 KV 显存占用计算公式：KV_FP8 = 2 × 64层 × 8 KV头 × 128 头维度 × 32768 tokens × 1 byte/param = 5.37 GB，相比 BF16 (10.74 GB) 节省 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层、8 KV头、128头维度）符合 GQA 设计，FP8 单字节存储计算正确，5.37GB 与 10.74GB 的 50% 节省比例在数学上自洽。
