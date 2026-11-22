# N146: 在 W4 权重 (13.55 GB) 下，启用 INT8 KV Cache 的总显存需求为 13.55 + 20.133 + 1.02 = 34.703 GB，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在 W4 权重 (13.55 GB) 下，启用 INT8 KV Cache 的总显存需求为 13.55 + 20.133 + 1.02 = 34.703 GB，超出单张 24 GB 显卡容量，必须使用双卡 (如 2x3090/2x4090) 或 48 GB+ 显卡 (如 A6000 Ada)。

## Corrected Claim

在 W4 权重 (13.55 GB) 下，启用 INT8 KV Cache 的总显存需求为 13.55 + 20.133 + 1.02 = 34.703 GB，超出单张 24 GB 显卡容量，必须使用双卡 (如 2x3090/2x4090) 或 48 GB+ 显卡 (如 A6000 Ada)。

## Evidence

先验知识/题面给定，逻辑校验通过：13.55+20.133+1.02=34.703，且34.703>24，结论符合显存计算逻辑
