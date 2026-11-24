# N494: 工作点C（分布式并行重建，高冗余）：利用软件定义存储或JBOD模式，将重建任务分散至所有在线节点的CPU和内存，绕过单一控制器瓶颈。假设有效聚合带宽可达 W_e

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

工作点C（分布式并行重建，高冗余）：利用软件定义存储或JBOD模式，将重建任务分散至所有在线节点的CPU和内存，绕过单一控制器瓶颈。假设有效聚合带宽可达 W_eff_C = 25 GB/s（受限于HDD物理极限和网络/总线饱和），则 T_rebuild_C = 400TB / 25GB/s = 16小时。需增加高速缓存或网络带宽投资，但RTO最短。

## Corrected Claim

工作点C（分布式并行重建，高冗余）：利用软件定义存储或JBOD模式，将重建任务分散至所有在线节点的CPU和内存，绕过单一控制器瓶颈。假设有效聚合带宽可达 W_eff_C = 25 GB/s（受限于HDD物理极限和网络/总线饱和），则 T_rebuild_C = 400TB / 25GB/s = 16小时。需增加高速缓存或网络带宽投资，但RTO最短。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB / 25GB/s = 16h 计算正确，分布式重建绕过单控制器瓶颈符合存储架构原理，25GB/s 聚合带宽在 HDD+网络场景下量级合理。
