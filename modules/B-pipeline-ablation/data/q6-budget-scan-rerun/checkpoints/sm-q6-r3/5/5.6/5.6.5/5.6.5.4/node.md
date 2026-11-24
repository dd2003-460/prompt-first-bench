# N308: 自建POP BGP路由切换期间受影响流量比例 $\phi_{switch}$ 的量化：基于BGP收敛时间$T_{bgp}=30-120s$，$\phi_{swi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115, N116, N117

## Claim

自建POP BGP路由切换期间受影响流量比例 $\phi_{switch}$ 的量化：基于BGP收敛时间$T_{bgp}=30-120s$，$\phi_{switch} = 1 - e^{-T_{bgp}/T_{dns\_cache}}$，若DNS缓存TTL=300s，$T_{bgp}=60s$，则$\phi_{switch} \approx 0.18$。

## Corrected Claim

自建POP BGP路由切换期间受影响流量比例 $\phi_{switch}$ 的量化：基于BGP收敛时间$T_{bgp}=30-120s$，$\phi_{switch} = 1 - e^{-T_{bgp}/T_{dns\_cache}}$，若DNS缓存TTL=300s，$T_{bgp}=60s$，则$\phi_{switch} \approx 0.18$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式计算 1 - e^(-60/300) = 1 - e^(-0.2) ≈ 0.181，与陈述一致；BGP收敛时间30-120s及DNS TTL 300s均为合理工程参数。

## Search Query

BGP convergence time impact on traffic distribution
