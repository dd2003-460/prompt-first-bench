# N185: FP8 激活/缓冲显存占用估算：基于 batch_size=1 和 seq_len=32K，中间层激活峰值约为 2.0-3.0 GB（取决于具体实现优化，保守取

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

FP8 激活/缓冲显存占用估算：基于 batch_size=1 和 seq_len=32K，中间层激活峰值约为 2.0-3.0 GB（取决于具体实现优化，保守取 3.0 GB 用于下限计算）

## Corrected Claim

FP8 激活/缓冲显存占用估算：基于 batch_size=1 和 seq_len=32K，中间层激活峰值约为 2.0-3.0 GB（取决于具体实现优化，保守取 3.0 GB 用于下限计算）

## Evidence

先验知识/题面给定，逻辑校验通过
