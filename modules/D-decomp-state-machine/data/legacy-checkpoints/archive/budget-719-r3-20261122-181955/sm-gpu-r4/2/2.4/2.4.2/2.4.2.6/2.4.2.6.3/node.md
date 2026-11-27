# N739: 32K 上下文长度下 BF16 KV Cache 总内存占用修正值：Total_KV = 256 KB/token * 32,768 tokens = 8,38

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N260

## Claim

32K 上下文长度下 BF16 KV Cache 总内存占用修正值：Total_KV = 256 KB/token * 32,768 tokens = 8,388,608 KB = 8.0 GB。N260 中的 4.30 GB 因层数错误减半，实际占用翻倍，直接决定单卡显存是否足够。

## Corrected Claim

32K 上下文长度下 BF16 KV Cache 总内存占用修正值：Total_KV = 256 KB/token * 32,768 tokens = 8,388,608 KB = 8.0 GB。N260 中的 4.30 GB 因层数错误减半，实际占用翻倍，直接决定单卡显存是否足够。

## Evidence

先验知识/题面给定，逻辑校验通过：256 KB/token * 32,768 tokens = 8,388,608 KB = 8.0 GB，计算无误且量级合理。
