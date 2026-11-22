# N702: RTX 4090 双卡 (48GB) 在 FP8 精度下支持 Batch Size 4-6，KV Cache 总占用约为 16.8 GB (4.2 GB * 4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N289, N290, N291

## Claim

RTX 4090 双卡 (48GB) 在 FP8 精度下支持 Batch Size 4-6，KV Cache 总占用约为 16.8 GB (4.2 GB * 4)，剩余 31.2 GB 用于权重和系统开销，支持更高并发吞吐量

## Corrected Claim

RTX 4090 双卡 (48GB) 在 FP8 精度下支持 Batch Size 4-6，KV Cache 总占用约为 16.8 GB (4.2 GB * 4)，剩余 31.2 GB 用于权重和系统开销，支持更高并发吞吐量

## Evidence

先验知识/题面给定，逻辑校验通过：48GB显存减去16.8GB KV Cache后剩余31.2GB，足以容纳主流大模型权重及系统开销，数值量级与工程常识一致。
