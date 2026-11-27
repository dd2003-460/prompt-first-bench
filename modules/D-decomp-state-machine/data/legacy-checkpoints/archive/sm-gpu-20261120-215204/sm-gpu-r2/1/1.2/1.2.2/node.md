# N42: Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Corrected Claim

Qwen3-27B 在 INT8 精度下，推理所需的总硬性显存需求为 47.48 GB，由 27 GB 权重显存与 20.48 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT8下权重约27GB，KV Cache 20.48GB，总和47.48GB，数值量级与计算逻辑自洽。
