# N282: RTX 5090 在 32K 上下文 BF16 下的显存可行性缺口：权重 55GB + KV Cache 1.2GB = 56.2GB > 32GB 显存，缺口

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

RTX 5090 在 32K 上下文 BF16 下的显存可行性缺口：权重 55GB + KV Cache 1.2GB = 56.2GB > 32GB 显存，缺口 24.2GB。因此单卡 5090 无法运行 BF16，必须使用 FP8 (权重 27.5GB + KV 1.2GB = 28.7GB < 32GB) 或 INT4 (权重 14GB + KV 1.2GB = 15.2GB < 32GB)

## Corrected Claim

RTX 5090 在 32K 上下文 BF16 下的显存可行性缺口：权重 55GB + KV Cache 1.2GB = 56.2GB > 32GB 显存，缺口 24.2GB。因此单卡 5090 无法运行 BF16，必须使用 FP8 (权重 27.5GB + KV 1.2GB = 28.7GB < 32GB) 或 INT4 (权重 14GB + KV 1.2GB = 15.2GB < 32GB)

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存为 32GB，BF16 权重 55GB 远超显存容量，FP8/INT4 量化后权重分别约为 27.5GB/14GB，加上 KV Cache 后均小于 32GB，数值量级与算术逻辑自洽。
