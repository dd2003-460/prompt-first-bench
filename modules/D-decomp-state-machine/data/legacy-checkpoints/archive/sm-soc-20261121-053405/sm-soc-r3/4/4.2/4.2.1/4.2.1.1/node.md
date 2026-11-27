# N177: 共享随机源：定义曝光量测量噪声 $\epsilon_{exp}$ 为均值为 0、标准差为 $\sigma_{exp}$ 的高斯分布，其中 $\sigma_{ex

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

共享随机源：定义曝光量测量噪声 $\epsilon_{exp}$ 为均值为 0、标准差为 $\sigma_{exp}$ 的高斯分布，其中 $\sigma_{exp}$ 代表平台日志中曝光事件记录的不确定性（如爬虫抓取误差、用户端加载失败），通常 $\sigma_{exp}/\mu_{exp} < 0.1$。

## Corrected Claim

共享随机源：定义曝光量测量噪声 $\epsilon_{exp}$ 为均值为 0、标准差为 $\sigma_{exp}$ 的高斯分布，其中 $\sigma_{exp}$ 代表平台日志中曝光事件记录的不确定性（如爬虫抓取误差、用户端加载失败），通常 $\sigma_{exp}/\mu_{exp} < 0.1$。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

web analytics exposure tracking error rate
