# N66: 单卡 RTX 4090 运行 Qwen3-27B 的可行性边界：FP8 权重 (27GB) + 32K KV Cache (8.4GB) = 35.4GB > 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

单卡 RTX 4090 运行 Qwen3-27B 的可行性边界：FP8 权重 (27GB) + 32K KV Cache (8.4GB) = 35.4GB > 24GB 显存，物理不可行；必须采用 INT4 (13.5GB) + KV Cache 量化 (INT8, 4.2GB) = 17.7GB，剩余 6.3GB 用于激活和框架开销，方可在单卡运行，此时质量损失显著增加。

## Corrected Claim

单卡 RTX 4090 运行 Qwen3-27B 的可行性边界：FP8 权重 (27GB) + 32K KV Cache (8.4GB) = 35.4GB > 24GB 显存，物理不可行；必须采用 INT4 (13.5GB) + KV Cache 量化 (INT8, 4.2GB) = 17.7GB，剩余 6.3GB 用于激活和框架开销，方可在单卡运行，此时质量损失显著增加。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型FP8权重约27GB，32K上下文KV Cache约8.4GB，总和35.4GB超过RTX 4090的24GB显存，物理不可行；INT4权重约13.5GB，INT8 KV Cache约4.2GB，总和17.7GB，剩余6.3GB用于激活和开销，符合单卡运行逻辑。

## Search Query

Qwen3-27B INT4 KV cache quantization single GPU feasibility
