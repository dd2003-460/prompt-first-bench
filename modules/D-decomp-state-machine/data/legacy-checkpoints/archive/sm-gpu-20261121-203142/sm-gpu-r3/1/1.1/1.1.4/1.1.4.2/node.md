# N135: 推理框架（如vLLM/TGI）的固定运行时开销（包括CUDA Context、cuDNN/FlashAttention工作区、临时缓冲区）通常占用 0.5-1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

推理框架（如vLLM/TGI）的固定运行时开销（包括CUDA Context、cuDNN/FlashAttention工作区、临时缓冲区）通常占用 0.5-1.5 GB 显存，这部分开销独立于模型权重和KV Cache，但在计算B_max时需从总显存中扣除，直接影响24GB显存卡上的可用余量。

## Corrected Claim

推理框架（如vLLM/TGI）的固定运行时开销（包括CUDA Context、cuDNN/FlashAttention工作区、临时缓冲区）通常占用 0.5-1.5 GB 显存，这部分开销独立于模型权重和KV Cache，但在计算B_max时需从总显存中扣除，直接影响24GB显存卡上的可用余量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM CUDA context overhead memory usage GB
