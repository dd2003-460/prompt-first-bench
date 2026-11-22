# N40: Apple M3 Ultra 512GB 统一内存带宽为 819GB/s (与M2 Ultra基本持平)，H100 SXM 带宽 3.35TB/s，带宽比为 4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Apple M3 Ultra 512GB 统一内存带宽为 819GB/s (与M2 Ultra基本持平)，H100 SXM 带宽 3.35TB/s，带宽比为 4.09:1；理论吞吐量比约为 0.244；M3 Ultra 的优势在于512GB容量可支持更大模型或更长上下文，但对于27B模型，其容量过剩 (512GB >> 56.2GB需求)，带宽瓶颈导致其吞吐量与M2 Ultra无显著差异，仅容量提升，性价比低于M2 Ultra

## Corrected Claim

Apple M3 Ultra 512GB 统一内存带宽为 819GB/s (与M2 Ultra基本持平)，H100 SXM 带宽 3.35TB/s，带宽比为 4.09:1；理论吞吐量比约为 0.244；M3 Ultra 的优势在于512GB容量可支持更大模型或更长上下文，但对于27B模型，其容量过剩 (512GB >> 56.2GB需求)，带宽瓶颈导致其吞吐量与M2 Ultra无显著差异，仅容量提升，性价比低于M2 Ultra

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 512GB 带宽 819GB/s 与 M2 Ultra 持平符合 Apple 官方规格；H100 SXM 带宽 3.35TB/s 符合 NVIDIA 官方数据；带宽比 3350/819 ≈ 4.09 计算正确；27B 模型 FP16 需求约 54-56GB，512GB 容量确实过剩，逻辑自洽。
