# N642: 工作点2（高负载/批量推理）：当并发序列数 max_num_seqs >= 8 且平均序列长度 > 8192 时，4x V100 集群的稳态功耗 P_high 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N229

## Claim

工作点2（高负载/批量推理）：当并发序列数 max_num_seqs >= 8 且平均序列长度 > 8192 时，4x V100 集群的稳态功耗 P_high ≈ 850W ± 80W（单卡 ~212.5W），此时内存带宽利用率 > 85%，功耗逼近 TDP 的 90% 以上，受限于显存访问延迟而非计算单元。

## Corrected Claim

工作点2（高负载/批量推理）：当并发序列数 max_num_seqs >= 8 且平均序列长度 > 8192 时，4x V100 集群处于高负载状态，稳态功耗接近 TDP 上限（通常 > 90%），主要受限于显存带宽而非计算单元。

## Evidence

[质询]该陈述包含具体的经验性功耗数值（850W ± 80W）和性能指标（内存带宽利用率 > 85%），这些并非第一性原理可推导的数学或物理常数，而是依赖于具体硬件配置、软件栈版本及负载特征的实测数据。在无来源支持的情况下，无法验证其准确性，且不同实现下数值可能存在显著差异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Tesla V100 SXM2 power consumption high load batch inference memory bandwidth limited watts
