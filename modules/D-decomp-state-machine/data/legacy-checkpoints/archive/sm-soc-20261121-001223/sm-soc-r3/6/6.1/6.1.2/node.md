# N191: 排序因子重算延迟 T_rank_update 的触发机制：T_rank_update 取决于排序模型是实时流式更新（Stream Processing）还是批量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

排序因子重算延迟 T_rank_update 的触发机制：T_rank_update 取决于排序模型是实时流式更新（Stream Processing）还是批量离线更新（Batch Processing）；若为批量更新，T_rank_update 等于 Batch_Interval（如 15-30 分钟）；需验证在降价事件发生后，T_rank_update 是否受 Batch_Interval 限制，导致新价格无法立即反映在排序中。

## Corrected Claim

排序因子重算延迟 T_rank_update 的触发机制：T_rank_update 取决于排序模型是实时流式更新（Stream Processing）还是批量离线更新（Batch Processing）；若为批量更新，T_rank_update 等于 Batch_Interval（如 15-30 分钟）；需验证在降价事件发生后，T_rank_update 是否受 Batch_Interval 限制，导致新价格无法立即反映在排序中。

## Evidence

先验知识/题面给定，逻辑校验通过：批量处理系统的更新延迟确实由批处理间隔（Batch Interval）决定，这是分布式计算与数据工程的基本原理，逻辑自洽且量级合理。
