# N442: GVisor 冷启动（无预热）耗时分解：T_cold = T_syscall_init + T_memory_mapping + T_process_fork，

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151

## Claim

GVisor 冷启动（无预热）耗时分解：T_cold = T_syscall_init + T_memory_mapping + T_process_fork，其中 T_syscall_init 通常占 60-70%（约 1.2-3.5s），T_memory_mapping 占 20-30%（约 0.4-1.5s），T_process_fork 占 10%（约 0.2-0.5s），总和 2-5s

## Corrected Claim

GVisor 冷启动耗时通常远低于传统容器，一般在毫秒至数百毫秒级别，具体分解取决于工作负载复杂度，但不应达到秒级（2-5s）量级。

## Evidence

[质询]GVisor 的核心优势之一是极快的启动速度（通常声称比传统容器快数倍，毫秒级或亚秒级），声称冷启动总耗时高达 2-5 秒且 syscall_init 占 1.2-3.5 秒，这与 GVisor 作为轻量级用户态内核的典型性能特征严重不符，极可能是将传统 Linux 容器或特定复杂场景下的数据误植，或者是量级错误（应为 ms 而非 s）。 | 先验知识/题面给定，逻辑校验未通过：GVisor 设计目标为低开销快速启动，2-5s 的冷启动时间违背其基本工程直觉和公开基准测试常识（通常为毫秒级），且无外部来源支持该具体数值分解。
