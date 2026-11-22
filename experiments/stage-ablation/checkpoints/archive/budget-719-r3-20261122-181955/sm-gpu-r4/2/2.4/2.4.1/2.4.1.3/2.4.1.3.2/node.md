# N720: FP8 精度下单卡可行性重评估：A6000 48GB 可运行 (27GB 权重 + 4GB KV Cache = 31GB < 48GB)，RTX 4090 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

FP8 精度下单卡可行性重评估：A6000 48GB 可运行 (27GB 权重 + 4GB KV Cache = 31GB < 48GB)，RTX 4090 24GB 不可行 (31GB > 24GB)，需 INT4 量化 (13.5GB 权重 + 4GB KV Cache = 17.5GB < 24GB) 才可行。

## Corrected Claim

FP8 精度下单卡可行性重评估：A6000 48GB 可运行 (27GB 权重 + 4GB KV Cache = 31GB < 48GB)，RTX 4090 24GB 不可行 (31GB > 24GB)，需 INT4 量化 (13.5GB 权重 + 4GB KV Cache = 17.5GB < 24GB) 才可行。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重27GB+KV 4GB=31GB，小于A6000 48GB显存，大于RTX 4090 24GB显存；INT4权重13.5GB+KV 4GB=17.5GB，小于RTX 4090 24GB显存，数值量级与算术逻辑均自洽。
