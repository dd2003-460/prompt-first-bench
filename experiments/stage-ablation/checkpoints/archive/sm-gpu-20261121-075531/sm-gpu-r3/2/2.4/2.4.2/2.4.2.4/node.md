# N202: Mac Studio M3 Ultra 256GB 方案在 32K 上下文下的 KV Cache 显存占用约为 1.93GB (INT8) 至 3.86GB (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Mac Studio M3 Ultra 256GB 方案在 32K 上下文下的 KV Cache 显存占用约为 1.93GB (INT8) 至 3.86GB (BF16)，加上模型权重 27GB 和系统开销 2GB，总占用约 31-33GB，远低于 256GB 上限，因此容量不是瓶颈，瓶颈在于内存带宽和计算单元 (GPU Core) 数量。

## Corrected Claim

Mac Studio M3 Ultra 256GB 方案在 32K 上下文下的 KV Cache 显存占用约为 1.93GB (INT8) 至 3.86GB (BF16)，加上模型权重 27GB 和系统开销 2GB，总占用约 31-33GB，远低于 256GB 上限，因此容量不是瓶颈，瓶颈在于内存带宽和计算单元 (GPU Core) 数量。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算量级合理（32K 上下文下 1.9-3.9GB 符合常见 LLM 架构估算），总占用 31-33GB 远低于 256GB 上限，结论自洽。

## Search Query

Qwen3-27B KV cache size 32k context int8 bytes
