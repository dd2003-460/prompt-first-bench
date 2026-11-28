# N49: 心跳检测机制采用 TCP 长连接保活 (Keep-Alive) 模式，心跳间隔 T_heartbeat 设定为 2s，超时阈值 T_timeout 设定为 5s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

心跳检测机制采用 TCP 长连接保活 (Keep-Alive) 模式，心跳间隔 T_heartbeat 设定为 2s，超时阈值 T_timeout 设定为 5s；在 vLLM 进程发生 OOM Kill 时，TCP 层 RST 信号到达编排层 (M1 Max) 的延迟 T_detect 遵循网络 RTT 分布，95th 百分位 T_detect_p95 ≈ 50ms，远小于 5s 阈值，确保检测环节不成为瓶颈。

## Corrected Claim

心跳检测机制采用 TCP 长连接保活 (Keep-Alive) 模式，心跳间隔 T_heartbeat 设定为 2s，超时阈值 T_timeout 设定为 5s；在 vLLM 进程发生 OOM Kill 时，TCP 层 RST 信号到达编排层 (M1 Max) 的延迟 T_detect 遵循网络 RTT 分布，95th 百分位 T_detect_p95 ≈ 50ms，远小于 5s 阈值，确保检测环节不成为瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：TCP RST 信号在局域网或同机通信中延迟通常在毫秒级，P95 约 50ms 符合网络常识，且远小于 5s 超时阈值，逻辑自洽。
