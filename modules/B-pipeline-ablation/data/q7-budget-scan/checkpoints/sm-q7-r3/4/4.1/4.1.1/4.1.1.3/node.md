# N286: 重建期间的业务停机时长 Downtime_hours = T_rebuild + T_detection (故障检测延迟，通常 <1分钟) + T_switch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

重建期间的业务停机时长 Downtime_hours = T_rebuild + T_detection (故障检测延迟，通常 <1分钟) + T_switchover (故障切换时间，通常 <1分钟)；对于内部数据湖，若采用热备或冗余阵列，业务停机时长可能仅为 T_switchover (秒级)，而数据重建在后台进行，此时 RTO 代价主要取决于 T_switchover 而非 T_rebuild。

## Corrected Claim

重建期间的业务停机时长 Downtime_hours = T_rebuild + T_detection (故障检测延迟，通常 <1分钟) + T_switchover (故障切换时间，通常 <1分钟)；对于内部数据湖，若采用热备或冗余阵列，业务停机时长可能仅为 T_switchover (秒级)，而数据重建在后台进行，此时 RTO 代价主要取决于 T_switchover 而非 T_rebuild。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了高可用架构中RTO（恢复时间目标）的构成逻辑，热备/冗余场景下停机时间确实主要取决于切换时间而非数据重建时间，符合分布式系统容灾设计的基本原理。

## Search Query

storage array failover time vs rebuild time RTO
