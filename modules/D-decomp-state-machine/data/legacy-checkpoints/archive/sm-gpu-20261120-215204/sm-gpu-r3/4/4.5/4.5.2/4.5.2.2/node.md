# N308: 修正项2（KV Cache每Token增量）：Qwen3-27B的KV Cache每Token增量 = 2 * 64层 * 8 KV头 * 128维 * 2 b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

修正项2（KV Cache每Token增量）：Qwen3-27B的KV Cache每Token增量 = 2 * 64层 * 8 KV头 * 128维 * 2 bytes = 262,144 bytes ≈ 0.25 MB/Token；32K上下文总KV Cache ≈ 8 GB，需从显存带宽中扣除这部分读取开销。

## Corrected Claim

修正项2（KV Cache每Token增量）：Qwen3-27B的KV Cache每Token增量 = 2 * 64层 * 8 KV头 * 128维 * 2 bytes = 262,144 bytes ≈ 0.25 MB/Token；32K上下文总KV Cache ≈ 8 GB，需从显存带宽中扣除这部分读取开销。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B架构参数（64层、8 KV头、128维）符合主流大模型设计，计算过程 2 * 64 * 8 * 128 * 2 = 262,144 bytes 准确，32K上下文总容量 262,144 * 32,768 ≈ 8.59 GB，与陈述中的 ≈ 8 GB 量级一致（考虑到实际部署中可能存在的对齐或近似处理，该数值在工程估算中合理）。
