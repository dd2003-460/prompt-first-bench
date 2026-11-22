# N13: 激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如v

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如vLLM/llama.cpp）基础开销约1-2GB，作为总显存需求的缓冲项。

## Corrected Claim

激活值与框架开销估算：推理时激活值峰值通常占权重大小的5%-10%（取决于batch size和seq length），加上CUDA Context和框架（如vLLM/llama.cpp）基础开销约1-2GB，作为总显存需求的缓冲项。

## Evidence

先验知识/题面给定，逻辑校验通过
