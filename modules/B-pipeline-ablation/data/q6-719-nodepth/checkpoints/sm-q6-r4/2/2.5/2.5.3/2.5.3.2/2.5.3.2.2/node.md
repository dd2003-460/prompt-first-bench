# N617: 空间权重修正后的边际延迟降低函数：ΔL_per_pop(N, region) = ΔL_base * exp(-N / N_decay) * W_region，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N203

## Claim

空间权重修正后的边际延迟降低函数：ΔL_per_pop(N, region) = ΔL_base * exp(-N / N_decay) * W_region，其中 W_region ∈ [0.5, 2.0] 反映区域用户密度权重，东部高密度区 W_region ≈ 1.5-2.0，西部低密度区 W_region ≈ 0.5-0.8

## Corrected Claim

空间权重修正后的边际延迟降低函数：ΔL_per_pop(N, region) = ΔL_base * exp(-N / N_decay) * W_region，其中 W_region ∈ [0.5, 2.0] 反映区域用户密度权重，东部高密度区 W_region ≈ 1.5-2.0，西部低密度区 W_region ≈ 0.5-0.8

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN regional user density weight POP placement optimization
