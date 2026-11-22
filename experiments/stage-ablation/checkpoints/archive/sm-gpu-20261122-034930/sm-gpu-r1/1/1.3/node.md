# N9: 推理框架（如vLLM）的额外显存开销（CUDA Context, Activation buffers）通常占总显存的5-10%，即约2.5-5GB，需从总显存

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

推理框架（如vLLM）的额外显存开销（CUDA Context, Activation buffers）通常占总显存的5-10%，即约2.5-5GB，需从总显存中预留。

## Corrected Claim

推理框架（如vLLM）的额外显存开销（CUDA Context, Activation buffers）通常占总显存的5-10%，即约2.5-5GB，需从总显存中预留。

## Evidence

先验知识/题面给定，逻辑校验通过
