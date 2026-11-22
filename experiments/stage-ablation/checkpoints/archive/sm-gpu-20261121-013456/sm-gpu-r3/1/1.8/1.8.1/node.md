# N71: 激活值/中间缓冲显存占用估算：对于 27B 模型，Batch Size=1 时，激活值开销约为 2.0 - 4.0 GB，取决于序列长度和是否启用 Flash 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

激活值/中间缓冲显存占用估算：对于 27B 模型，Batch Size=1 时，激活值开销约为 2.0 - 4.0 GB，取决于序列长度和是否启用 Flash Attention (Flash Attention 可减少 50% 激活显存)

## Corrected Claim

激活值/中间缓冲显存占用估算：对于 27B 模型，Batch Size=1 时，激活值开销约为 2.0 - 4.0 GB，取决于序列长度和是否启用 Flash Attention (Flash Attention 可减少 50% 激活显存)

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型在BS=1时，激活值显存占用主要取决于序列长度和层数，2-4GB的量级符合常规Transformer架构在中等序列长度（如2k-4k）下的估算范围，且Flash Attention减少激活显存的描述符合技术原理。

## Search Query

LLM inference activation memory footprint 27B model flash attention
