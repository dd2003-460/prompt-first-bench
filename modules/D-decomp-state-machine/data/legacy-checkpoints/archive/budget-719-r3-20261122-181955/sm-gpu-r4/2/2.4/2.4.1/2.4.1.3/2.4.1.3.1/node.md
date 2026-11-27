# N719: BF16 精度下单卡可行性修正：A100 80GB PCIe 可运行 (54GB 权重 + 8GB KV Cache = 62GB < 80GB)，H100 8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

BF16 精度下单卡可行性修正：A100 80GB PCIe 可运行 (54GB 权重 + 8GB KV Cache = 62GB < 80GB)，H100 80GB 可运行，但 A6000 48GB 不可行 (62GB > 48GB)，RTX 4090 24GB 不可行，修正 N254 中 'A6000 可行' 的错误。

## Corrected Claim

BF16 精度下单卡可行性修正：A100 80GB PCIe 可运行 (54GB 权重 + 8GB KV Cache = 62GB < 80GB)，H100 80GB 可运行，但 A6000 48GB 不可行 (62GB > 48GB)，RTX 4090 24GB 不可行，修正 N254 中 'A6000 可行' 的错误。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下54GB权重+8GB KV Cache=62GB，小于A100/H100的80GB显存，大于A6000的48GB和RTX 4090的24GB显存，数值比较逻辑自洽。
