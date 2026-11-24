# N316: 公有云CDN故障切换时间（Failover_Time_Cloud）基于Anycast路由收敛或DNS TTL刷新，通常<5s（Anycast）或<60s（DNS

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

公有云CDN故障切换时间（Failover_Time_Cloud）基于Anycast路由收敛或DNS TTL刷新，通常<5s（Anycast）或<60s（DNS）；自建POP若采用静态路由或BGP宣告撤销，Failover_Time_Self ≈ 30-120s（BGP收敛时间），若需手动切换则>300s。

## Corrected Claim

公有云CDN故障切换时间（Failover_Time_Cloud）基于Anycast路由收敛或DNS TTL刷新，通常<5s（Anycast）或<60s（DNS）；自建POP若采用静态路由或BGP宣告撤销，Failover_Time_Self ≈ 30-120s（BGP收敛时间），若需手动切换则>300s。

## Evidence

先验知识/题面给定，逻辑校验通过：Anycast基于路由收敛通常秒级，DNS受TTL限制通常分钟级，BGP收敛典型为30-120s，手动切换更慢，符合网络工程常识。
