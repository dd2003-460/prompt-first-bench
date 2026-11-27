# N118: PyTorch CUDA Context 基础开销量化：在 PyTorch 2.0+ 中，仅初始化 CUDA 上下文（不含模型加载）的显存占用通常为 300-5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

PyTorch CUDA Context 基础开销量化：在 PyTorch 2.0+ 中，仅初始化 CUDA 上下文（不含模型加载）的显存占用通常为 300-500 MB，该值随 CUDA 版本和驱动更新略有波动，但不随模型参数量或序列长度线性增长。

## Corrected Claim

PyTorch CUDA Context 基础开销量化：在 PyTorch 2.0+ 中，仅初始化 CUDA 上下文（不含模型加载）的显存占用通常为 300-500 MB，该值随 CUDA 版本和驱动更新略有波动，但不随模型参数量或序列长度线性增长。

## Evidence

先验知识/题面给定，逻辑校验通过
