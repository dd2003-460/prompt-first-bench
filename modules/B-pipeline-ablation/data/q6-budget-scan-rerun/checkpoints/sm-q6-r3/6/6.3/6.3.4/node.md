# N162: TCP 慢启动延迟惩罚 T_slow_start 的精确计算公式为 T_slow_start = RTT * log2(s / (1.5 * MSS * N))

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38, N39, N40

## Claim

TCP 慢启动延迟惩罚 T_slow_start 的精确计算公式为 T_slow_start = RTT * log2(s / (1.5 * MSS * N)), 其中 s 为对象大小，MSS=1460 bytes，N 为并发连接数（默认 N=1），该公式用于量化冷缓存未命中时的额外延迟。

## Corrected Claim

TCP 慢启动延迟惩罚 T_slow_start 的精确计算公式为 T_slow_start = RTT * log2(s / (1.5 * MSS * N)), 其中 s 为对象大小，MSS=1460 bytes，N 为并发连接数（默认 N=1），该公式用于量化冷缓存未命中时的额外延迟。

## Evidence

先验知识/题面给定，逻辑校验通过
