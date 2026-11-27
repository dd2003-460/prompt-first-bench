# N84: 单次故障的平均停机时间（MTTR）估算：消费级卡故障通常表现为驱动崩溃或显存错误，需重启服务，MTTR约0.5-2小时；数据中心卡具备冗余和热插拔，MTTR约1

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点3（故障恢复的自动化程度对比）与父节点中的MTTR估算高度重合，且其描述的‘恢复时间’实际上构成了MTTR的主要部分，导致概念重叠。此外，子节点1关注检测时间（MTTD），子节点3关注恢复时间，两者共同构成MTTR，但子节点3直接给出了具体的恢复时长，与父节点中关于MTTR的总时长描述存在逻辑上的包含关系而非正交分解。）

## Search Query

GPU mean time to repair inference service downtime
