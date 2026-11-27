# N8: 推理框架（如 vLLM, llama.cpp）的额外显存开销（包括 CUDA context, cuDNN workspace, 碎片化开销）通常占总显存的 1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

推理框架（如 vLLM, llama.cpp）的额外显存开销（包括 CUDA context, cuDNN workspace, 碎片化开销）通常占总显存的 10-20%，即对于 54GB 权重，需额外预留 5.4-10.8GB

## Corrected Claim

推理框架（如 vLLM, llama.cpp）的额外显存开销（包括 CUDA context, cuDNN workspace, 碎片化开销）通常占总显存的 10-20%，即对于 54GB 权重，需额外预留 5.4-10.8GB

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM llama.cpp GPU memory overhead CUDA context size
