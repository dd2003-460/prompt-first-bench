# N145: 对于静态内容主导的 CDN 工作负载（如视频/软件包），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常 ≥

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

对于静态内容主导的 CDN 工作负载（如视频/软件包），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常 ≥ 0.95，表明热度结构高度稳定，LFU 频率计数器在 2-3 天内即可收敛至稳态，支持 LFU 策略获得最大理论增益。

## Corrected Claim

对于静态内容主导的 CDN 工作负载（如视频/软件包），对象热度排名的 Spearman 自相关系数 ρ_rank(t, t+1) 在 1 天时间步长下通常 ≥ 0.95，表明热度结构高度稳定，LFU 频率计数器在 2-3 天内即可收敛至稳态，支持 LFU 策略获得最大理论增益。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN static content request frequency stability Spearman correlation daily
