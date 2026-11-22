# N202: 修正后的 FP8 单卡最小显存需求：权重 27.8 GB + KV Cache 0.95 GB + 激活/框架 3 GB = 31.75 GB；因此 24GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

修正后的 FP8 单卡最小显存需求：权重 27.8 GB + KV Cache 0.95 GB + 激活/框架 3 GB = 31.75 GB；因此 24GB 卡 (RTX 4090/L4) 仍不可行（31.75 > 24），但 48GB 卡 (L40S) 可行（31.75 < 48），且留有 16.25 GB 空间用于增加 batch size 或更长上下文。

## Corrected Claim

修正后的 FP8 单卡最小显存需求：权重 27.8 GB + KV Cache 0.95 GB + 激活/框架 3 GB = 31.75 GB；因此 24GB 卡 (RTX 4090/L4) 仍不可行（31.75 > 24），但 48GB 卡 (L40S) 可行（31.75 < 48），且留有 16.25 GB 空间用于增加 batch size 或更长上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（27.8+0.95+3=31.75），显存对比逻辑自洽（31.75>24, 31.75<48），剩余空间计算正确（48-31.75=16.25）。
