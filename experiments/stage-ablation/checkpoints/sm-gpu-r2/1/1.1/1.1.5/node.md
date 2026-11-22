# N43: 激活值 (Activations) 与临时缓冲区显存估算：对于单请求 (Batch=1) 推理，激活值显存占用与序列长度和隐藏层维度成正比，通常估算为 2-5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

激活值 (Activations) 与临时缓冲区显存估算：对于单请求 (Batch=1) 推理，激活值显存占用与序列长度和隐藏层维度成正比，通常估算为 2-5 GB (包含 LayerNorm, Attention 中间结果, GEMM 缓冲区)。

## Corrected Claim

激活值 (Activations) 与临时缓冲区显存估算：对于单请求 (Batch=1) 推理，激活值显存占用与序列长度和隐藏层维度成正比，通常估算为 2-5 GB (包含 LayerNorm, Attention 中间结果, GEMM 缓冲区)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference activation memory footprint batch size 1
