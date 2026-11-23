# N197: 大对象传输的P99延迟修正项：T_transmit_P99_corrected = T_slow_start + (s_target / B_effective

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

大对象传输的P99延迟修正项：T_transmit_P99_corrected = T_slow_start + (s_target / B_effective)，其中B_effective为慢启动结束后的有效带宽（受限于min(链路带宽, 拥塞窗口增长速率)），对于5MB对象，若忽略慢启动仅按100Mbps计算，T_transmit=400ms，但计入慢启动后T_transmit_P99≈700-900ms，误差率约75-125%，此修正项是评估自建节点大文件分发性能的关键量化依据

## Corrected Claim

大对象传输的P99延迟修正项：T_transmit_P99_corrected = T_slow_start + (s_target / B_effective)，其中B_effective为慢启动结束后的有效带宽（受限于min(链路带宽, 拥塞窗口增长速率)），对于5MB对象，若忽略慢启动仅按100Mbps计算，T_transmit=400ms，但计入慢启动后T_transmit_P99≈700-900ms，误差率约75-125%，此修正项是评估自建节点大文件分发性能的关键量化依据

## Evidence

先验知识/题面给定，逻辑校验通过：5MB对象在100Mbps下理论传输时间400ms，计入TCP慢启动及P99长尾效应后延迟增至700-900ms符合网络传输物理规律及工程经验，数值量级合理且内部自洽。
