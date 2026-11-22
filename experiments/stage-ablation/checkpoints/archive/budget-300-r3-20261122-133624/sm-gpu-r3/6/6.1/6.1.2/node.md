# N407: 32K 上下文下 KV Cache 总占用：64 KB/token * 32,768 tokens = 2,097,152 KB = 2 GB；加上 INT8 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

32K 上下文下 KV Cache 总占用：64 KB/token * 32,768 tokens = 2,097,152 KB = 2 GB；加上 INT8 权重 27 GB 和框架开销 2 GB，总需求 = 31 GB，远超 24 GB 显存，确认单卡 INT8 不可行。

## Corrected Claim

32K 上下文下 KV Cache 总占用：64 KB/token * 32,768 tokens = 2,097,152 KB = 2 GB；加上 INT8 权重 27 GB 和框架开销 2 GB，总需求 = 31 GB，远超 24 GB 显存，确认单卡 INT8 不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算 (64KB * 32768 = 2GB) 及总显存需求 (2+27+2=31GB) 均符合算术逻辑，且 31GB > 24GB 的结论成立。
