# N146: 对于动态内容主导的 CDN 工作负载（如新闻/社交信息流），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

对于动态内容主导的 CDN 工作负载（如新闻/社交信息流），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常介于 0.6-0.8，表明热度结构中等稳定，LFU 增益受限，需结合 LRU 时间衰减机制（如 LFU with aging）以平衡新鲜度与频率偏好。

## Corrected Claim

对于动态内容主导的 CDN 工作负载（如新闻/社交信息流），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常介于 0.6-0.8，表明热度结构中等稳定，LFU 增益受限，需结合 LRU 时间衰减机制（如 LFU with aging）以平衡新鲜度与频率偏好。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN dynamic content request frequency volatility daily Spearman correlation
