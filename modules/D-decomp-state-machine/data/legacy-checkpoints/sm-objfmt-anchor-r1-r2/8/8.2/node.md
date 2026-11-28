# N109: Steady-State Throughput (Tps) 与 ITL 的数学关系为 ITL_ms = 1000 / Tps_tokens_per_sec；因此

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Steady-State Throughput (Tps) 与 ITL 的数学关系为 ITL_ms = 1000 / Tps_tokens_per_sec；因此，'ITL < 50ms' 等价于 'Tps > 20 tokens/sec'，'ITL < 200ms' 等价于 'Tps > 5 tokens/sec'。性价比优化目标函数 Maximize(Tps) 实际上隐式包含了确保 Tps > 5 的硬约束。

## Corrected Claim

Steady-State Throughput (Tps) 与 ITL 的数学关系为 ITL_ms = 1000 / Tps_tokens_per_sec；因此，'ITL < 50ms' 等价于 'Tps > 20 tokens/sec'，'ITL < 200ms' 等价于 'Tps > 5 tokens/sec'。性价比优化目标函数 Maximize(Tps) 实际上隐式包含了确保 Tps > 5 的硬约束。

## Evidence

先验知识/题面给定，逻辑校验通过：ITL（Inter-Token Latency）定义为生成单个token的平均时间，与吞吐量Tps互为倒数关系（单位换算后），数学推导自洽。
