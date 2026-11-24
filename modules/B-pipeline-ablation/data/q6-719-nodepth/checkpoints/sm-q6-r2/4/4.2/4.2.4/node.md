# N107: 自建 POP 处理延迟 T_proc_pop_p99 (ms)，受限于单机 CPU 核心数、内存带宽及磁盘 I/O，典型 P99 值在 2-10ms 之间，与公

- **status**: verified
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

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted CDN server processing latency benchmark
