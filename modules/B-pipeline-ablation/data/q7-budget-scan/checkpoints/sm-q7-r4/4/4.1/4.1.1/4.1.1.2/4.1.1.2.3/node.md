# N667: 重建期间性能降级导致的业务损失成本量化：假设重建期间存储系统 I/O 延迟增加 50%，导致关键扫描任务超时。若每小时业务损失价值为 ¥1,000（基于机会成本

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N230

## Claim

重建期间性能降级导致的业务损失成本量化：假设重建期间存储系统 I/O 延迟增加 50%，导致关键扫描任务超时。若每小时业务损失价值为 ¥1,000（基于机会成本 N88 的一部分），则 C_rebuild_downtime = T_rebuild_hours * ¥1,000/h * Degradation_Factor。若 Degradation_Factor=0.5（性能减半），T_rebuild=342h，则 C_rebuild_downtime ≈ 342 * 1000 * 0.5 = ¥171,000/次重建事件。

## Corrected Claim

重建期间性能降级导致的业务损失成本量化：假设重建期间存储系统 I/O 延迟增加 50%，导致关键扫描任务超时。若每小时业务损失价值为 ¥1,000（基于机会成本 N88 的一部分），则 C_rebuild_downtime = T_rebuild_hours * ¥1,000/h * Degradation_Factor。若 Degradation_Factor=0.5（性能减半），T_rebuild=342h，则 C_rebuild_downtime ≈ 342 * 1000 * 0.5 = ¥171,000/次重建事件。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 342 * 1000 * 0.5 = 171,000 正确，公式定义与变量代入一致，无逻辑矛盾。
