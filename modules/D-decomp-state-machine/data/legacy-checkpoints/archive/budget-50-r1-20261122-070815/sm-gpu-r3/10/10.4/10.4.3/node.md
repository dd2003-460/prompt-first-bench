# N429: RTX 4090 24GB 显存无法单卡运行 Qwen3-27B INT8 模型（权重 27GB + KV Cache 2GB > 24GB），因此 N148 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

RTX 4090 24GB 显存无法单卡运行 Qwen3-27B INT8 模型（权重 27GB + KV Cache 2GB > 24GB），因此 N148 中'INT8 是更好替代'的论断在单卡场景下不成立；若采用双卡 2x RTX 4090，INT8 方案总显存 48GB 可行，但需评估双卡通信开销及 TCO，此时 INT8 相比 INT4 的质量优势（<1% vs 2-5% 损失）需与成本增加（$3200 vs $1600）进行权衡。

## Corrected Claim

RTX 4090 24GB 显存无法单卡运行 Qwen3-27B INT8 模型（权重 27GB + KV Cache 2GB > 24GB），因此 N148 中'INT8 是更好替代'的论断在单卡场景下不成立；若采用双卡 2x RTX 4090，INT8 方案总显存 48GB 可行，但需评估双卡通信开销及 TCO，此时 INT8 相比 INT4 的质量优势（<1% vs 2-5% 损失）需与成本增加（$3200 vs $1600）进行权衡。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB权重+2GB KV Cache=29GB > 24GB显存，单卡不可行；双卡48GB > 29GB，可行。数值量级与逻辑推导自洽。
