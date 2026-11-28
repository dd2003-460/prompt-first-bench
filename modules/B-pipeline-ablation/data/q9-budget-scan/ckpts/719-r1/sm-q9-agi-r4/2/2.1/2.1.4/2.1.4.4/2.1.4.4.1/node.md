# N450: GVisor 中 read/write 系统调用的单次平均延迟为 2.5μs-5μs（用户态内核转发开销），而非 N154 引用的 50ms（50ms 通常指进

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

GVisor 中 read/write 系统调用的单次平均延迟为 2.5μs-5μs（用户态内核转发开销），而非 N154 引用的 50ms（50ms 通常指进程冷启动或完整容器初始化开销，需区分 steady-state syscall 与 cold-start 开销）

## Corrected Claim

GVisor 中 read/write 系统调用的单次平均延迟通常在微秒级（约 2.5μs-5μs，具体取决于硬件和配置），显著低于进程冷启动或完整容器初始化的毫秒级开销（如 50ms），需区分 steady-state syscall 与 cold-start 开销。

## Evidence

[质询]缺乏直接来源支持具体的 2.5μs-5μs 数值范围，且不同硬件/配置下 GVisor 的系统调用开销可能存在波动，该具体数值区间属于经验测量数据，无法仅凭逻辑推导确定。 | 经验事实，逻辑自洽（GVisor 用户态内核转发开销确实在微秒级，远小于毫秒级的冷启动开销），但缺来源支持具体数值区间。

## Search Query

GVisor syscall latency benchmark microseconds read write
