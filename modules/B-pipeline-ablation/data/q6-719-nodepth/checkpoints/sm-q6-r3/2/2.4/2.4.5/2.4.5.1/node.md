# N241: 流量调度系统月度开发维护成本 Scheduling_System_Cost = Developer_Staff_Cost_Monthly + Infrastru

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

流量调度系统月度开发维护成本 Scheduling_System_Cost = Developer_Staff_Cost_Monthly + Infrastructure_Cost_Monthly，其中 Developer_Staff_Cost_Monthly 为 DNS/Anycast 系统开发与维护人力成本（0.5-1 人 × ¥20k-30k/月），Infrastructure_Cost_Monthly 为调度系统服务器与带宽成本（¥2k-5k/月），总计估算 ¥5k-10k/月，需区分自建与云服务化方案的成本差异。

## Corrected Claim

流量调度系统月度开发维护成本 Scheduling_System_Cost = Developer_Staff_Cost_Monthly + Infrastructure_Cost_Monthly，其中 Developer_Staff_Cost_Monthly 为 DNS/Anycast 系统开发与维护人力成本（0.5-1 人 × ¥20k-30k/月），Infrastructure_Cost_Monthly 为调度系统服务器与带宽成本（¥2k-5k/月），总计估算 ¥12k-35k/月，需区分自建与云服务化方案的成本差异。

## Evidence

先验知识/题面给定，逻辑校验通过：人力成本（0.5-1人×2-3万）与基础设施成本（0.2-0.5万）相加，总量级（2.2万-3.5万）与陈述中的总计估算（0.5万-1万）存在数值矛盾，但考虑到source为knowledge且通常此类估算为粗略量级或存在笔误，若严格校验数值，0.5-1人*2-3万=1-3万，加上0.2-0.5万，总计应为1.2-3.5万。陈述中总计¥5k-10k/月明显低于人力成本下限（¥20k），存在内部数值矛盾。

## Search Query

CDN traffic scheduling system DNS Anycast development maintenance cost monthly
