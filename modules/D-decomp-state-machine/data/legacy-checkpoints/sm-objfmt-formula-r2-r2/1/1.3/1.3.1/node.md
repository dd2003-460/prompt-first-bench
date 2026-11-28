# N40: vLLM 推理框架的固定运行时开销（包括 CUDA Context、cuDNN 工作区、NCCL 通信缓冲等）约为 1-2GB，该开销与模型大小无关，主要取决于

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

vLLM 推理框架的固定运行时开销（包括 CUDA Context、cuDNN 工作区、NCCL 通信缓冲等）约为 1-2GB，该开销与模型大小无关，主要取决于 GPU 架构和驱动版本。

## Corrected Claim

vLLM 推理框架的固定运行时开销（包括 CUDA Context、cuDNN 工作区、NCCL 通信缓冲等）约为 1-2GB，该开销与模型大小无关，主要取决于 GPU 架构和驱动版本。

## Evidence

先验知识/题面给定，逻辑校验通过
