# N111: 针对 N34 中 seq_len=32k 的场景，单次 All-Reduce 通信的启动延迟（launch overhead）通常在 5-10 μs 量级，在高

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

针对 N34 中 seq_len=32k 的场景，单次 All-Reduce 通信的启动延迟（launch overhead）通常在 5-10 μs 量级，在高频小消息通信中会显著抵消带宽优势，需纳入实际耗时修正项。

## Corrected Claim

针对 N34 中 seq_len=32k 的场景，单次 All-Reduce 通信的启动延迟（launch overhead）通常在 5-10 μs 量级，在高频小消息通信中会显著抵消带宽优势，需纳入实际耗时修正项。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NCCL allreduce latency small message overhead microseconds
