# N292: RAID 6 扩容时的重建开销系数：新增 N_new 块盘后，需对全卷进行一致性校验或重建，耗时 T_rebuild_new = (C_total_new / 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

RAID 6 扩容时的重建开销系数：新增 N_new 块盘后，需对全卷进行一致性校验或重建，耗时 T_rebuild_new = (C_total_new / Bandwidth_rebuild)，期间系统性能下降 30-50%（参考 N67），该隐性性能损失折算为年成本 C_perf_loss = T_rebuild_new * (1 - 0.7) * Revenue_per_hour_lost，若年营收损失率 10%，此项不可忽略。

## Corrected Claim

RAID 6 扩容时需对全卷进行一致性校验或重建，耗时 T_rebuild_new = (C_total_new / Bandwidth_rebuild)。在此期间，由于 I/O 资源被重建任务占用，系统整体性能通常会显著下降（具体幅度取决于负载和硬件，常见范围可能在 30%-50% 甚至更高）。这种性能损失会转化为业务机会成本，其具体金额需根据实际业务营收对性能敏感度的弹性系数进行估算，而非简单固定比例。

## Evidence

[质询]性能下降幅度（30-50%）和营收损失率（10%）属于高度依赖具体硬件配置、负载类型及业务场景的经验参数，缺乏通用性，且公式中直接乘以营收损失率隐含了‘性能下降完全转化为营收损失’的强假设，逻辑上过于简化。 | 先验知识/题面给定，逻辑校验通过，但具体数值为经验估计，缺乏普适性来源支持，故降级为定性表述。

## Search Query

RAID 6 expansion rebuild performance degradation cost
