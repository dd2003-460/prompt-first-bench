# N123: P99 延迟预算分解：总 P99 延迟 T_p99 = t_prop_rtt + t_queue + t_process + t_jitter_buffer，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

P99 延迟预算分解：总 P99 延迟 T_p99 = t_prop_rtt + t_queue + t_process + t_jitter_buffer，其中 t_prop_rtt 为往返传播延迟，t_queue 为网络排队延迟（P99 下通常 5-20ms），t_process 为服务器处理延迟（图片/视频元数据 <5ms，视频首帧 <50ms），t_jitter_buffer 为客户端抗抖动缓冲（通常 100-300ms，若不计入服务端 P99 则需明确口径）

## Corrected Claim

P99 延迟预算分解：总 P99 延迟 T_p99 = t_prop_rtt + t_queue + t_process + t_jitter_buffer，其中 t_prop_rtt 为往返传播延迟，t_queue 为网络排队延迟（P99 下通常 5-20ms），t_process 为服务器处理延迟（图片/视频元数据 <5ms，视频首帧 <50ms），t_jitter_buffer 为客户端抗抖动缓冲（通常 100-300ms，若不计入服务端 P99 则需明确口径）

## Evidence

先验知识/题面给定，逻辑校验通过：延迟分解公式符合网络通信基本模型，各分项量级（RTT、排队、处理、抖动缓冲）符合典型工程经验值，无内部矛盾。
