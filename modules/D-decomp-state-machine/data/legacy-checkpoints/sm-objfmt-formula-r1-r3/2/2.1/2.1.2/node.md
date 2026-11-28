# N55: FP8 (E4M3) 精度下 Qwen3-27B 的权重存储体积精确计算值为 26.98 GB (26.98B * 1 byte / 1e9)，且无需额外的 B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

FP8 (E4M3) 精度下 Qwen3-27B 的权重存储体积精确计算值为 26.98 GB (26.98B * 1 byte / 1e9)，且无需额外的 Block-wise Scale 因子存储（假设使用标准 FP8 格式）

## Corrected Claim

FP8 (E4M3) 精度下 Qwen3-27B 的权重存储体积精确计算值为 26.98 GB (26.98B * 1 byte / 1e9)，且无需额外的 Block-wise Scale 因子存储（假设使用标准 FP8 格式）

## Evidence

先验知识/题面给定，逻辑校验通过：26.98B参数 * 1字节/参数 = 26.98GB，且标准FP8 E4M3格式本身不包含Block-wise Scale因子（该特性通常属于MXFP8等变体），计算与描述自洽。
