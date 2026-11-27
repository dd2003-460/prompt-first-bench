# N138: TP=4 Decode 阶段单步 All-Reduce 通信延迟主导项：Kernel Launch 与同步开销约为 5-10μs/step (N56)，占单 T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

TP=4 Decode 阶段单步 All-Reduce 通信延迟主导项：Kernel Launch 与同步开销约为 5-10μs/step (N56)，占单 Token 生成时间 (~12.5ms @ 80tok/s) 的比例为 0.04%-0.08%，远低于 N70 声称的 20-30% 吞吐损失，表明通信开销非主要瓶颈。

## Corrected Claim

TP=4 Decode 阶段单步 All-Reduce 通信延迟主导项：Kernel Launch 与同步开销约为 5-10μs/step (N56)，占单 Token 生成时间 (~12.5ms @ 80tok/s) 的比例为 0.04%-0.08%，远低于 N70 声称的 20-30% 吞吐损失，表明通信开销非主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：5-10μs 相对于 12.5ms (12,500μs) 的比例计算正确 (0.04%-0.08%)，且符合 GPU Kernel Launch 微秒级开销与 Decode 毫秒级延迟的量级常识。
