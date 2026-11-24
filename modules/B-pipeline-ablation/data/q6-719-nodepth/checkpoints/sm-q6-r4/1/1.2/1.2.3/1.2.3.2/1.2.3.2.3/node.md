# N478: T_processing（处理延迟）分解：T_processing = T_switching + T_queue_internal。T_switching 为

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

T_processing（处理延迟）分解：T_processing = T_switching + T_queue_internal。T_switching 为硬件交换芯片转发延迟（典型 1-5μs，可忽略），T_queue_internal 为网卡队列与内核协议栈处理延迟。在 10Gbps 高负载下，Linux 内核协议栈处理单包延迟约为 10-50μs，但受上下文切换影响，P99 处理延迟可达 1-2ms，主要瓶颈在软中断处理效率。

## Corrected Claim

T_processing（处理延迟）分解：T_processing = T_switching + T_queue_internal。T_switching 为硬件交换芯片转发延迟（典型 1-5μs，可忽略），T_queue_internal 为网卡队列与内核协议栈处理延迟。在 10Gbps 高负载下，Linux 内核协议栈处理单包延迟约为 10-50μs，但受上下文切换影响，P99 处理延迟可达 1-2ms，主要瓶颈在软中断处理效率。

## Evidence

先验知识/题面给定，逻辑校验通过
