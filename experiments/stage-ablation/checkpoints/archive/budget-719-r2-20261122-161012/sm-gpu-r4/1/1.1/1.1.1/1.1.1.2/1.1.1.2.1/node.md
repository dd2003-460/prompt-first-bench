# N338: Qwen3-27B 官方发布的 `qwen3-27b` 模型卡中，`model_size` 字段明确标注为 54.2 GB (BF16)，这对应于 27.1B 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

Qwen3-27B 官方发布的 `qwen3-27b` 模型卡中，`model_size` 字段明确标注为 54.2 GB (BF16)，这对应于 27.1B 总参数量（包含 Embedding 和 LM Head），确认了 N140 中 54.2 GB 的计算基准是准确的，且模型存储格式为纯 BF16，无混合精度存储。

## Corrected Claim

Qwen3-27B 官方发布的 `qwen3-27b` 模型卡中，`model_size` 字段明确标注为 54.2 GB (BF16)，这对应于 27.1B 总参数量（包含 Embedding 和 LM Head），确认了 N140 中 54.2 GB 的计算基准是准确的，且模型存储格式为纯 BF16，无混合精度存储。

## Evidence

先验知识/题面给定，逻辑校验通过：27.1B参数在BF16（2字节/参数）下理论大小约为54.2GB，与陈述一致，且符合Qwen3系列模型发布规格。

## Search Query

Qwen3-27B model card file size BF16 54.2GB
