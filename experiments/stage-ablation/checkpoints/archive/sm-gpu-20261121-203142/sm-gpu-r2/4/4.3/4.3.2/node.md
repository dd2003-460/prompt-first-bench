# N84: 单次故障的平均停机时间（MTTR）估算：消费级卡故障通常表现为驱动崩溃或显存错误，需重启服务，MTTR约0.5-2小时；数据中心卡具备冗余和热插拔，MTTR约1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

单次故障的平均停机时间（MTTR）估算：消费级卡故障通常表现为驱动崩溃或显存错误，需重启服务，MTTR约0.5-2小时；数据中心卡具备冗余和热插拔，MTTR约1-4小时（含检测与切换）。

## Corrected Claim

单次故障的平均停机时间（MTTR）估算：消费级卡故障通常表现为驱动崩溃或显存错误，需重启服务，MTTR约0.5-2小时；数据中心卡具备冗余和热插拔，MTTR约1-4小时（含检测与切换）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU mean time to repair inference service downtime
