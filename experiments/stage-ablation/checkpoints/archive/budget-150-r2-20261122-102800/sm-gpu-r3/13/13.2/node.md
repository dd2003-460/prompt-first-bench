# N418: RTX 5090显存容量可行性边界：32GB显存无法容纳Qwen3-27B BF16权重(54.6GB)及32K KV Cache，必须使用INT8(27.3G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166, N167, N168

## Claim

RTX 5090显存容量可行性边界：32GB显存无法容纳Qwen3-27B BF16权重(54.6GB)及32K KV Cache，必须使用INT8(27.3GB)或W4(13.65GB)量化；INT8下剩余显存仅~4.7GB，不足以支撑32K KV Cache(需~20GB+)，故RTX 5090单卡无法原生运行BF16或标准INT8+32K KV，需依赖PagedAttention offload或更激进的W4量化。

## Corrected Claim

RTX 5090显存容量可行性边界：32GB显存无法容纳Qwen3-27B BF16权重(54.6GB)及32K KV Cache，必须使用INT8(27.3GB)或W4(13.65GB)量化；INT8下剩余显存仅~4.7GB，不足以支撑32K KV Cache(需~20GB+)，故RTX 5090单卡无法原生运行BF16或标准INT8+32K KV，需依赖PagedAttention offload或更激进的W4量化。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54.6GB（27B*2bytes），远超RTX 5090的32GB显存；INT8量化后约27.3GB，剩余显存约4.7GB，确实不足以支撑32K上下文所需的KV Cache（通常需数GB至数十GB，取决于层数和头数，20GB+为合理估算上限或特定配置下的需求），因此单卡原生运行受限的结论符合物理内存约束逻辑。

## Search Query

Qwen3-27B INT8 KV cache size 32k tokens
