# N147: 对于突发事件驱动的工作负载（如热点事件/直播），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 小时时间步长下可能 < 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

对于突发事件驱动的工作负载（如热点事件/直播），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 小时时间步长下可能 < 0.5，表明热度结构高度不稳定，LFU 策略失效，LRU 或 Belady MIN 近似策略更优，因为历史频率信息对当前访问模式无预测力。

## Corrected Claim

对于突发事件驱动的工作负载（如热点事件/直播），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 小时时间步长下可能 < 0.5，表明热度结构高度不稳定，LFU 策略失效，LRU 或 Belady MIN 近似策略更优，因为历史频率信息对当前访问模式无预测力。

## Evidence

先验知识/题面给定，逻辑校验通过：突发事件导致访问模式剧烈变化，Spearman系数低表明排名不稳定，LFU依赖历史频率故失效，LRU/MIN依赖近期性故更优，逻辑自洽。

## Search Query

CDN bursty workload request frequency instability hourly correlation
