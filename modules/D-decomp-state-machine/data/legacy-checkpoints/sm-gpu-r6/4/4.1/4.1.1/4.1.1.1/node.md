# N165: Qwen3-27B INT8 量化下的模型权重大小为 27GB (27B params * 1 byte)；在 RTX 4090 (24GB) 上，仅权重即超出

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

Qwen3-27B INT8 量化下的模型权重大小为 27GB (27B params * 1 byte)；在 RTX 4090 (24GB) 上，仅权重即超出显存 3GB，因此单卡 INT8 不可行，必须使用 Offload 或 W4 量化；若使用 W4 (4-bit) 量化，权重大小约为 13.5GB，剩余 10.5GB 可用于 KV Cache 和激活值。

## Corrected Claim

Qwen3-27B INT8 量化下的模型权重大小为 27GB (27B params * 1 byte)；在 RTX 4090 (24GB) 上，仅权重即超出显存 3GB，因此单卡 INT8 不可行，必须使用 Offload 或 W4 量化；若使用 W4 (4-bit) 量化，权重大小约为 13.5GB，剩余 10.5GB 可用于 KV Cache 和激活值。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT8量化后权重约27GB，超过RTX 4090的24GB显存，单卡不可行；W4量化后权重约13.5GB，剩余10.5GB可用于KV Cache和激活值，数值量级与逻辑均合理。

## Search Query

Qwen3-27B INT8 weight size GB calculation
