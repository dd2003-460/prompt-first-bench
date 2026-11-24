# N297: 缓存命中率下降 ΔCHR_limit 与回源带宽超限比例 R_over 的关系：ΔCHR_limit = R_over * (1 - CHR_base)，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

缓存命中率下降 ΔCHR_limit 与回源带宽超限比例 R_over 的关系：ΔCHR_limit = R_over * (1 - CHR_base)，其中 CHR_base=0.75（N117给定），若 R_over=0.2（20%请求超限），则 ΔCHR_limit ≈ 0.2 * 0.25 = 5%，导致回源带宽增加 5%

## Corrected Claim

缓存命中率下降 ΔCHR_limit 与回源带宽超限比例 R_over 的关系：ΔCHR_limit = R_over * (1 - CHR_base)，其中 CHR_base=0.75（N117给定），若 R_over=0.2（20%请求超限），则 ΔCHR_limit ≈ 0.2 * 0.25 = 5%，导致回源带宽增加 5%

## Evidence

先验知识/题面给定，逻辑校验通过
