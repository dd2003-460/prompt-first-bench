# N107: 自建 POP 处理延迟 T_proc_pop_p99 (ms)，受限于单机 CPU 核心数、内存带宽及磁盘 I/O，典型 P99 值在 2-10ms 之间，与公

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

自建 POP 处理延迟 T_proc_pop_p99 (ms)，受限于单机 CPU 核心数、内存带宽及磁盘 I/O，典型 P99 值在 2-10ms 之间，与公有云 CDN 边缘节点的处理延迟处于同一数量级，但可能因硬件老化或配置差异而波动。

## Corrected Claim

自建 POP 处理延迟 T_proc_pop_p99 (ms)，受限于单机 CPU 核心数、内存带宽及磁盘 I/O，典型 P99 值在 2-10ms 之间，与公有云 CDN 边缘节点的处理延迟处于同一数量级，但可能因硬件老化或配置差异而波动。

## Evidence

父节点级核验未通过：不完备（子节点分别描述了基准值、磁盘I/O影响和CPU负载影响，三者维度不同且无逻辑矛盾，正交性良好。但父节点明确提到‘受限于单机CPU核心数、内存带宽及磁盘I/O’，子节点覆盖了磁盘和CPU，却遗漏了‘内存带宽’这一关键限制因素，导致完备性不足。）

## Search Query

self-hosted CDN server processing latency benchmark
