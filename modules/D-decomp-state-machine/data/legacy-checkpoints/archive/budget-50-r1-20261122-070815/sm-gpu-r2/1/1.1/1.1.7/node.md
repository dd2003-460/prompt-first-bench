# N41: 激活值显存开销 (C_activation) 主要取决于批处理大小 (batch_size) 和序列长度，对于单用户推理 (batch_size=1)，在 32

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

激活值显存开销 (C_activation) 主要取决于批处理大小 (batch_size) 和序列长度，对于单用户推理 (batch_size=1)，在 32K 上下文下通常可忽略不计（< 1 GB），但在高并发场景下需按 2 * hidden_dim * seq_len * batch_size * dtype_size 估算。

## Corrected Claim

激活值显存开销 (C_activation) 主要取决于批处理大小 (batch_size) 和序列长度，对于单用户推理 (batch_size=1)，在 32K 上下文下通常可忽略不计（< 1 GB），但在高并发场景下需按 2 * hidden_dim * seq_len * batch_size * dtype_size 估算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference activation memory footprint calculation batch size
