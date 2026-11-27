# N161: Qwen3-27B 的 FFN 层采用 SwiGLU 激活函数，其结构包含三个线性投影矩阵（gate_proj, up_proj, down_proj），中间激

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Qwen3-27B 的 FFN 层采用 SwiGLU 激活函数，其结构包含三个线性投影矩阵（gate_proj, up_proj, down_proj），中间激活维度为 Intermediate_Size。

## Corrected Claim

Qwen3-27B 的 FFN 层采用 SwiGLU 激活函数，其结构包含三个线性投影矩阵（gate_proj, up_proj, down_proj），中间激活维度为 Intermediate_Size。

## Evidence

先验知识/题面给定，逻辑校验通过
