# N91: 基于内存带宽受限假设，M3 Ultra 运行 Qwen3-27B (BF16, 54GB) 的理论最大 TPS = Memory_Bandwidth / (KV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

基于内存带宽受限假设，M3 Ultra 运行 Qwen3-27B (BF16, 54GB) 的理论最大 TPS = Memory_Bandwidth / (KV_Cache_Size_Per_Token + Weight_Access_Per_Token)。若 Weight_Access 主导，TPS ≈ 800GB/s / 54GB ≈ 14.8 TPS (理论峰值)，实际因计算开销通常降至 5-10 TPS。

## Corrected Claim

基于内存带宽受限假设，M3 Ultra 运行 Qwen3-27B (BF16, 54GB) 的理论最大 TPS = Memory_Bandwidth / (KV_Cache_Size_Per_Token + Weight_Access_Per_Token)。若 Weight_Access 主导，TPS ≈ 800GB/s / 54GB ≈ 14.8 TPS (理论峰值)，实际因计算开销通常降至 5-10 TPS。

## Evidence

先验知识/题面给定，逻辑校验通过：M3 Ultra 内存带宽约 800GB/s，Qwen3-27B BF16 权重约 54GB，理论峰值 800/54 ≈ 14.8 TPS 符合内存带宽受限模型的基本物理直觉，实际 5-10 TPS 的衰减范围也符合工程经验。
