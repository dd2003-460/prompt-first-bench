# N336: vLLM/SGLang 框架在 A100 上的基础运行时开销（CUDA Context, cuDNN Handle, PyTorch Runtime, 日志缓冲

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

vLLM/SGLang 框架在 A100 上的基础运行时开销（CUDA Context, cuDNN Handle, PyTorch Runtime, 日志缓冲等）固定占用约为 0.8-1.2GB，该部分不随 Batch Size 变化，但受 CUDA 版本和驱动配置影响，需预留 1.5GB 作为安全边际。

## Corrected Claim

vLLM/SGLang 框架在 A100 上的基础运行时开销（CUDA Context, cuDNN Handle, PyTorch Runtime, 日志缓冲等）固定占用约为 0.8-1.2GB，该部分不随 Batch Size 变化，但受 CUDA 版本和驱动配置影响，需预留 1.5GB 作为安全边际。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM CUDA context memory overhead A100 base runtime footprint
