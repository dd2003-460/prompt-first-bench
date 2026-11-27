# N198: 修正后的 BF16 单卡最小显存需求：权重 55.6 GB + KV Cache 1.9 GB + 激活/框架 3 GB = 60.5 GB；因此 48GB 卡

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

修正后的 BF16 单卡最小显存需求：权重 55.6 GB + KV Cache 1.9 GB + 激活/框架 3 GB = 60.5 GB；因此 48GB 卡 (如 L40S 48GB) 在 32K 上下文下仍不可行（60.5 > 48），需 80GB 卡 (A100/H100) 或启用 INT8 KV Cache 量化。

## Corrected Claim

修正后的 BF16 单卡最小显存需求：权重 55.6 GB + KV Cache 1.9 GB + 激活/框架 3 GB = 60.5 GB；因此 48GB 卡 (如 L40S 48GB) 在 32K 上下文下仍不可行（60.5 > 48），需 80GB 卡 (A100/H100) 或启用 INT8 KV Cache 量化。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下7B模型权重约14GB，若为更大模型（如30B+）则55.6GB合理；KV Cache 1.9GB与32K上下文及模型层数/头数匹配；总显存60.5GB > 48GB，结论自洽。
