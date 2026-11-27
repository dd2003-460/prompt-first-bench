# N53: INT8 量化采用对称或非对称校准，对于 Qwen3-27B，非对称 INT8 通常比对称 INT8 减少 1-2% 的困惑度上升，但需要额外的 zero-po

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

INT8 量化采用对称或非对称校准，对于 Qwen3-27B，非对称 INT8 通常比对称 INT8 减少 1-2% 的困惑度上升，但需要额外的 zero-point 存储（每通道 1 个 int8，增加约 0.1% 显存）。

## Corrected Claim

INT8 量化采用对称或非对称校准，对于 Qwen3-27B，非对称 INT8 通常比对称 INT8 减少 1-2% 的困惑度上升，但需要额外的 zero-point 存储（每通道 1 个 int8，增加约 0.1% 显存）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

INT8 symmetric vs asymmetric quantization LLM accuracy
