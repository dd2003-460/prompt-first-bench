# N74: FP8 KV Cache 在 H100 (Hopper, SM 9.0) 上的原生硬件加速支持状态：SM 9.0 原生支持 FP8 Tensor Cores，可

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

FP8 KV Cache 在 H100 (Hopper, SM 9.0) 上的原生硬件加速支持状态：SM 9.0 原生支持 FP8 Tensor Cores，可实现 2x 于 BF16 的矩阵乘法吞吐，KV Cache 读取带宽需求降低至 BF16 的 50%。

## Corrected Claim

FP8 KV Cache 在 H100 (Hopper, SM 9.0) 上的原生硬件加速支持状态：SM 9.0 原生支持 FP8 Tensor Cores，可实现 2x 于 BF16 的矩阵乘法吞吐，KV Cache 读取带宽需求降低至 BF16 的 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 (SM 9.0) 确实原生支持 FP8 Tensor Cores，其矩阵乘法吞吐量约为 BF16 的 2 倍，且 FP8 数据宽度为 BF16 的一半，因此 KV Cache 读取带宽需求降低至 50%。

## Search Query

H100 SM 9.0 FP8 tensor core native support bandwidth reduction
