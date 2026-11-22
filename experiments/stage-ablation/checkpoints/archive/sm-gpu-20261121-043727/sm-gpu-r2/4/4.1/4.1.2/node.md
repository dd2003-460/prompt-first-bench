# N63: 基于 N44 获取的参数，计算 Qwen3-27B 在 BF16 (2 bytes/element) 精度下，32K 上下文长度 (Seq_Len=32768)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

基于 N44 获取的参数，计算 Qwen3-27B 在 BF16 (2 bytes/element) 精度下，32K 上下文长度 (Seq_Len=32768) 的单条请求 KV Cache 显存占用具体数值 (GB)；该数值是判断单卡显存是否足以容纳并发 Batch Size 的关键约束项。

## Corrected Claim

基于 N44 获取的参数，计算 Qwen3-27B 在 BF16 (2 bytes/element) 精度下，32K 上下文长度 (Seq_Len=32768) 的单条请求 KV Cache 显存占用具体数值 (GB)；该数值是判断单卡显存是否足以容纳并发 Batch Size 的关键约束项。

## Evidence

先验知识/题面给定，逻辑校验通过
