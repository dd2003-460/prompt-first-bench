# N71: PyTorch/CUDA 默认内存分配器（Caching Allocator）在动态形状输入下，显存碎片化导致的不可用显存比例通常介于 5%-15% 之间，具体

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

PyTorch/CUDA 默认内存分配器（Caching Allocator）在动态形状输入下，显存碎片化导致的不可用显存比例通常介于 5%-15% 之间，具体数值取决于 batch size 变化频率

## Corrected Claim

PyTorch/CUDA 默认内存分配器（Caching Allocator）在动态形状输入下，显存碎片化导致的不可用显存比例通常介于 5%-15% 之间，具体数值取决于 batch size 变化频率

## Evidence

先验知识/题面给定，逻辑校验通过
