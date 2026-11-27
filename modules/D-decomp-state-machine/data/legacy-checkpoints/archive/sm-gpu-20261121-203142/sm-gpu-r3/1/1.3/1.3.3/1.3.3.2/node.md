# N150: Qwen3-27B 在 32K 上下文、INT8 量化 KV Cache 下的显存占用：Size = 6.44 GB (BF16) * 0.5 = 3.22 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Qwen3-27B 在 32K 上下文、INT8 量化 KV Cache 下的显存占用：Size = 6.44 GB (BF16) * 0.5 = 3.22 GB，相比 BF16 节省 3.22 GB 显存

## Corrected Claim

Qwen3-27B 在 32K 上下文、INT8 量化 KV Cache 下的显存占用：Size = 6.44 GB (BF16) * 0.5 = 3.22 GB，相比 BF16 节省 3.22 GB 显存

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化通常将显存占用减半（2字节变1字节），6.44GB * 0.5 = 3.22GB，节省量等于原占用的一半，计算与逻辑自洽。
