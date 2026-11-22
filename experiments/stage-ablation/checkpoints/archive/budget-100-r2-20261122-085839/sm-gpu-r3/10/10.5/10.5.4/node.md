# N319: 启用 FP8 KV Cache 后的总显存需求 = 权重 54.2GB + KV Cache (FP8) 6.29GB + 开销 ~10GB ≈ 70.49GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

启用 FP8 KV Cache 后的总显存需求 = 权重 54.2GB + KV Cache (FP8) 6.29GB + 开销 ~10GB ≈ 70.49GB，剩余显存 9.51GB，可支持 Batch=2 或 64K 上下文，满足 32K 容量下限且留有安全余量

## Corrected Claim

启用 FP8 KV Cache 后的总显存需求 = 权重 54.2GB + KV Cache (FP8) 6.29GB + 开销 ~10GB ≈ 70.49GB，剩余显存 9.51GB，可支持 Batch=2 或 64K 上下文，满足 32K 容量下限且留有安全余量

## Evidence

先验知识/题面给定，逻辑校验通过：54.2 + 6.29 + 10 = 70.49GB，80GB - 70.49GB = 9.51GB，数值计算自洽，符合FP8量化显存估算逻辑。
