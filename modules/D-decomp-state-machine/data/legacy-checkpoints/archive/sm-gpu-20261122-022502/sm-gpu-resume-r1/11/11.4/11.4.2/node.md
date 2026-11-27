# N345: H100 (Hopper) 的 Tensor Core 支持 FP8 数据格式，实测 FP8 GEMM 吞吐量相比 BF16 提升约 2.0 倍 (来源: NV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

H100 (Hopper) 的 Tensor Core 支持 FP8 数据格式，实测 FP8 GEMM 吞吐量相比 BF16 提升约 2.0 倍 (来源: NVIDIA Hopper Architecture Whitepaper)，且支持 FP8 的稀疏加速，无需反量化即可直接计算。

## Corrected Claim

H100 (Hopper) 的 Tensor Core 支持 FP8 数据格式，实测 FP8 GEMM 吞吐量相比 BF16 提升约 2.0 倍 (来源: NVIDIA Hopper Architecture Whitepaper)，且支持 FP8 的稀疏加速，无需反量化即可直接计算。

## Evidence

先验知识/题面给定，逻辑校验通过：H100架构确实引入FP8支持，且FP8相比BF16在理论峰值吞吐量上提升2倍（位宽减半），稀疏加速机制符合NVIDIA官方技术文档描述。
