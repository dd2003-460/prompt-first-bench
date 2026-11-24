# N695: 公有云CDN回源流量成本在高缓存命中率工作点（Hit_Rate_Cloud = 95%，对应核心区域热门对象预热充分场景）的量化值：Origin_Fetch_T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N240

## Claim

公有云CDN回源流量成本在高缓存命中率工作点（Hit_Rate_Cloud = 95%，对应核心区域热门对象预热充分场景）的量化值：Origin_Fetch_Traffic_GB = 2,000,000 GB × 0.05 = 100,000 GB，Cloud_Origin_Fetch_Cost = 100,000 × ¥0.15 = ¥15,000/月，此工作点回源成本最低，适合长尾内容占比低的场景。

## Corrected Claim

公有云CDN回源流量成本在高缓存命中率工作点（Hit_Rate_Cloud = 95%，对应核心区域热门对象预热充分场景）的量化值：Origin_Fetch_Traffic_GB = 2,000,000 GB × 0.05 = 100,000 GB，Cloud_Origin_Fetch_Cost = 100,000 × ¥0.15 = ¥15,000/月，此工作点回源成本最低，适合长尾内容占比低的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（2,000,000 * 0.05 = 100,000; 100,000 * 0.15 = 15,000），且符合CDN回源成本随命中率升高而降低的基本经济逻辑。

## Search Query

Alibaba Cloud CDN origin fetch traffic pricing high cache hit rate scenario
