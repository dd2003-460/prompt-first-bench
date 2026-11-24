# N126: 自建 POP 节点的处理时间 T_proc_pop P99，通常高于公有云 CDN（5-10ms vs 1-5ms），因自建硬件性能较低且缺乏大规模分布式调度优

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

自建 POP 节点的处理时间 T_proc_pop P99，通常高于公有云 CDN（5-10ms vs 1-5ms），因自建硬件性能较低且缺乏大规模分布式调度优化，取决于单机 CPU 和内存配置。

## Corrected Claim

自建 POP 节点的处理时间 T_proc_pop P99，通常高于公有云 CDN（5-10ms vs 1-5ms），因自建硬件性能较低且缺乏大规模分布式调度优化，取决于单机 CPU 和内存配置。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-built CDN node processing time latency benchmark
