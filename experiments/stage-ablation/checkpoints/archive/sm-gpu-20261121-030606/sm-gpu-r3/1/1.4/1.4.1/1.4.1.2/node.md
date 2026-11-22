# N210: Mac Studio M2 Ultra 统一内存架构的带宽-延迟权衡：虽然标称带宽 1.2TB/s，但 CPU-GPU 共享内存导致延迟敏感型操作（如 KV C

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Mac Studio M2 Ultra 统一内存架构的带宽-延迟权衡：虽然标称带宽 1.2TB/s，但 CPU-GPU 共享内存导致延迟敏感型操作（如 KV Cache 随机访问）的 effective bandwidth 降至理论值的 60-70%；对于 32K 上下文，KV Cache 访问模式为顺序写入+随机读取，实测 effective bandwidth 可能仅为 800 GB/s，修正后吞吐量 = 800 / (13.5 + 5.2 + 2.5) ≈ 37.6 tokens/s，仍远高于 N95 的 3-5 tokens/s，表明 N95 数据可能存在测量环境错误（如未关闭后台进程或未预热缓存）。

## Corrected Claim

Mac Studio M2 Ultra 统一内存架构标称带宽约 1.2TB/s，但 CPU-GPU 共享内存可能导致延迟敏感型操作的有效带宽低于理论值；对于长上下文 KV Cache 访问，实际吞吐量受限于内存延迟和带宽共享，具体数值需依赖实测数据，不能仅凭理论带宽简单推算。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如60-70%的效率系数、800GB/s的实测带宽、37.6 tokens/s的吞吐量），这些并非第一性原理可推导的数学或物理定律，而是依赖于特定硬件微架构、内存控制器调度策略及具体工作负载的复杂经验数据。虽然量级在逻辑上大致合理（M2 Ultra带宽确实约为1.2TB/s，且共享内存确实存在延迟开销），但缺乏直接来源支持这些精确的实测数值，且‘N95数据可能存在测量环境错误’属于推测性结论，缺乏实证依据。 | 经验事实，逻辑自洽但缺来源支持；M2 Ultra带宽量级正确，但具体效率系数和吞吐量数值无法从第一性原理严格推出，且无外部来源验证。
