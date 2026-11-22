# N60: CUDA Context 开销 ≈ 100-200MB per GPU，cuDNN/cuBLAS 库加载开销 ≈ 200-500MB，PyTorch 运行时基础

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

CUDA Context 开销 ≈ 100-200MB per GPU，cuDNN/cuBLAS 库加载开销 ≈ 200-500MB，PyTorch 运行时基础开销 ≈ 300-500MB，总计 ≈ 600MB-1.2GB（不含模型权重和激活）

## Corrected Claim

CUDA Context 开销 ≈ 100-200MB per GPU，cuDNN/cuBLAS 库加载开销 ≈ 200-500MB，PyTorch 运行时基础开销 ≈ 300-500MB，总计 ≈ 600MB-1.2GB（不含模型权重和激活）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead PyTorch runtime baseline memory usage
