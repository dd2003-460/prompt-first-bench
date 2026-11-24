# N674: JBOD 无硬件冗余的单盘故障恢复时间 RTO_hw 计算：RTO_hw = max(T_detect, T_replace, T_sync)，其中 T_syn

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N233

## Claim

JBOD 无硬件冗余的单盘故障恢复时间 RTO_hw 计算：RTO_hw = max(T_detect, T_replace, T_sync)，其中 T_sync = V_object_size / T_replication_bw，对于 1MB 对象和 10Gbps 网络，T_sync ≈ 0.008s/对象，但并发同步受限于磁盘 IOPS，需计算 IOPS 瓶颈下的总同步时间。

## Corrected Claim

JBOD 无硬件冗余的单盘故障恢复时间 RTO_hw 计算：RTO_hw = max(T_detect, T_replace, T_sync)，其中 T_sync = V_object_size / T_replication_bw，对于 1MB 对象和 10Gbps 网络，T_sync ≈ 0.008s/对象，但并发同步受限于磁盘 IOPS，需计算 IOPS 瓶颈下的总同步时间。

## Evidence

先验知识/题面给定，逻辑校验通过：1MB对象在10Gbps带宽下传输时间约为0.008s，量级合理；JBOD无冗余导致单盘故障需全量数据重建，RTO由检测、更换及同步时间最大值决定，符合存储系统恢复逻辑。
