# N127: 能效比指标 Tokens/Watt 的计算需区分 Idle 和 Active 状态，对于本地工作站，若日均使用 8 小时，加权平均功耗 P_avg = (P_i

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

能效比指标 Tokens/Watt 的计算需区分 Idle 和 Active 状态，对于本地工作站，若日均使用 8 小时，加权平均功耗 P_avg = (P_idle * 16h + P_active * 8h) / 24h，最终能效指标为 TPS_active / P_avg，用于对比不同架构（如 Mac Studio 低待机功耗 vs GPU 高待机功耗）的长期经济性。

## Corrected Claim

能效比指标 Tokens/Watt 的计算需区分 Idle 和 Active 状态。对于本地工作站，若已知日均活跃时间，可通过加权平均计算总功耗 P_avg，进而计算长期能效指标 TPS_active / P_avg，以评估不同架构（如低待机功耗 vs 高待机功耗设备）的长期经济性。

## Evidence

[质询]该陈述包含具体的经验性假设（如“日均使用8小时”、“Mac Studio低待机功耗”的具体对比结论），这些属于特定场景下的工程经验或市场数据，无法从第一性原理严格推导，且参考来源主要讨论数据中心/工厂级能效，未直接覆盖本地工作站的具体加权公式及特定硬件对比。 | 逻辑自洽（加权平均功耗计算符合物理直觉，TPW定义合理），但参考来源[1][2][3]主要聚焦于数据中心/芯片级能效，未直接支持本地工作站的具体时间加权公式及特定硬件对比，属于经验事实缺直接来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29061425/article/details/165402269&rut=ecfebc96d2a5ee440fb5b33fa267f5ca9639252b07f931d7f098ed64606e0e3d', 'type': 'ddg', 'title': 'AI基础设施能效革命：从算力竞赛到每瓦Token优化-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29038303/article/details/167336293&rut=644c129fb38edc895750ddae436116923730dcb54a245e26a7485290be3d0a52', 'type': 'ddg', 'title': '从PUE到TPW：算电协同Agent如何优化每瓦Token产出 - CSDN博客'}
- {'url': 'https://wattthe.net/tools/inference-tokens-per-watt-calculator/&rut=8e1b92e80387e885a6f83fbc482fbd2143fdff350fb6d28ecb88091824c3849b', 'type': 'ddg', 'title': 'Inference Tokens-per-Watt Calculator: AI Efficiency'}
