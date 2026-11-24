# N327: POP迁移成本 (Migration_Cost) 包含硬件重置成本 (Hardware_Reset_Cost ≈ ¥50k) 和数据预热时间成本 (Data_W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

POP迁移成本 (Migration_Cost) 包含硬件重置成本 (Hardware_Reset_Cost ≈ ¥50k) 和数据预热时间成本 (Data_Warmup_Cost = T_warmup × Lost_Traffic_Value)，其中 T_warmup 为缓存重新命中所需时间（约 24-48h），Lost_Traffic_Value 为预热期间因缓存未命中导致的额外回源带宽成本，估算为 ¥5k-¥10k。

## Corrected Claim

POP迁移成本 (Migration_Cost) 包含硬件重置成本 (Hardware_Reset_Cost ≈ ¥50k) 和数据预热时间成本 (Data_Warmup_Cost = T_warmup × Lost_Traffic_Value)，其中 T_warmup 为缓存重新命中所需时间（约 24-48h），Lost_Traffic_Value 为预热期间因缓存未命中导致的额外回源带宽成本，估算为 ¥5k-¥10k。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node migration cost data warmup time penalty
