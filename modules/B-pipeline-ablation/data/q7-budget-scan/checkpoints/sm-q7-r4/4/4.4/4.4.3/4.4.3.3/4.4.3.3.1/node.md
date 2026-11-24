# N816: 两阶段提交(2PC)的一致性窗口 T_consistency_2PC = 2 * RTT + T_commit_log；假设 RTT=10ms, T_commi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N304

## Claim

两阶段提交(2PC)的一致性窗口 T_consistency_2PC = 2 * RTT + T_commit_log；假设 RTT=10ms, T_commit_log=5ms（本地 NVMe 写入延迟），则 T_consistency_2PC = 25ms；若 RTT 波动至 50ms，T_consistency_2PC = 105ms

## Corrected Claim

两阶段提交(2PC)的一致性窗口 T_consistency_2PC = 2 * RTT + T_commit_log；假设 RTT=10ms, T_commit_log=5ms（本地 NVMe 写入延迟），则 T_consistency_2PC = 25ms；若 RTT 波动至 50ms，T_consistency_2PC = 105ms

## Evidence

先验知识/题面给定，逻辑校验通过：2PC一致性窗口通常包含协调者到参与者的往返（2*RTT）及日志持久化时间，数值计算 2*10+5=25 和 2*50+5=105 准确无误。
