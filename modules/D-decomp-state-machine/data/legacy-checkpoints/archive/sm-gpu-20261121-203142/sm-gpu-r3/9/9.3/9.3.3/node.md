# N358: Apple M2 Ultra 在 32K 上下文下，若采用 INT4 量化权重并配合 CPU Offload 部分 KV Cache，Prefill 阶段因 P

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

Apple M2 Ultra 在 32K 上下文下，若采用 INT4 量化权重并配合 CPU Offload 部分 KV Cache，Prefill 阶段因 PCIe 瓶颈导致实际耗时可能超过 30 秒，此为低性能高兼容性工作点，仅适用于对 TTFT 无严格要求的批处理场景。

## Corrected Claim

Apple M2 Ultra 在 32K 上下文下，若采用 INT4 量化权重并配合 CPU Offload 部分 KV Cache，Prefill 阶段因 PCIe 带宽远低于统一内存带宽，实际耗时将显著高于纯 GPU/统一内存方案，可能达到数十秒量级，此为低性能高兼容性工作点，仅适用于对 TTFT 无严格要求的批处理场景。

## Evidence

[质询]该陈述包含具体的性能数值（>30秒）和特定的硬件瓶颈归因（PCIe），属于经验事实。虽然M2 Ultra的PCIe带宽（~64GB/s）确实远低于其统一内存带宽（~800GB/s），导致CPU Offload KV Cache在Prefill阶段成为瓶颈是合理的物理推断，但'30秒'这一具体阈值缺乏通用基准测试支持，且高度依赖于模型大小、具体量化实现及系统负载，存在将特定场景数据泛化为普遍规律的风险。 | 经验事实，逻辑自洽（PCIe带宽瓶颈导致Offload性能下降符合物理直觉），但缺来源直接支持具体数值，故降级。

## Search Query

Apple M2 Ultra INT4 quantization prefill latency overhead
