# N223: Qwen3-27B 的 Hidden_Size 实际值为 4096，Layer 数为 48，此参数直接决定 AllReduce 通信量的分子大小，若模型版本更新

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

Qwen3-27B 的 Hidden_Size 实际值为 4096，Layer 数为 48，此参数直接决定 AllReduce 通信量的分子大小，若模型版本更新导致 Layer 数或 Hidden_Size 变化，需重新计算总通信量。

## Corrected Claim

Qwen3-27B 的 Hidden_Size 实际值为 4096，Layer 数为 48，此参数直接决定 AllReduce 通信量的分子大小，若模型版本更新导致 Layer 数或 Hidden_Size 变化，需重新计算总通信量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B hidden size num layers config
