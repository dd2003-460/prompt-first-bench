# N447: 数据中心 GPU 的故障模式分布 (Failure Mode Distribution)：基于 Google 数据中心 GPU 集群日志分析，显存 (HBM) 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146

## Claim

数据中心 GPU 的故障模式分布 (Failure Mode Distribution)：基于 Google 数据中心 GPU 集群日志分析，显存 (HBM) 故障占比约 40%，计算核心 (SM) 故障占比约 30%，电源/接口故障占比约 30%，不同故障模式的 MTTR 差异显著，需分别计算加权平均停机时间。

## Corrected Claim

数据中心 GPU 的故障模式分布因硬件代际和负载而异，通常显存 (HBM) 和计算核心 (SM) 是主要故障源，电源/接口故障占比相对较低，不同故障模式的 MTTR 差异显著，需分别计算加权平均停机时间。

## Evidence

[质询]具体数值（40%/30%/30%）缺乏公开权威来源直接支持，且不同研究（如Google SRE论文、其他数据中心报告）中故障模式分布可能因硬件代际、负载类型而异，存在将特定案例泛化为普遍规律的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

datacenter GPU failure mode distribution HBM vs SM Google logs
