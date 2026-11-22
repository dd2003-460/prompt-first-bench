# N319: Mac Studio M2 Ultra 在长上下文 (32K+) 场景下的内存碎片化风险：由于缺乏 PagedAttention 等优化技术，KV Cache 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

Mac Studio M2 Ultra 在长上下文 (32K+) 场景下的内存碎片化风险：由于缺乏 PagedAttention 等优化技术，KV Cache 管理效率低于 NVIDIA 方案，当上下文长度 >64K 或 Batch>2 时，内存碎片化可能导致实际可用显存减少 10-20%，使理论吞吐上限从 13.1 tokens/s 降至 10-11 tokens/s。

## Corrected Claim

Mac Studio M2 Ultra 在长上下文 (32K+) 场景下，由于缺乏 PagedAttention 等优化技术，KV Cache 管理效率可能低于 NVIDIA 方案。当上下文长度 >64K 或 Batch>2 时，内存碎片化可能导致实际可用显存显著减少，从而降低理论吞吐上限。

## Evidence

[质询]该陈述包含具体的性能衰减数值（10-20%）和吞吐上限（13.1 tokens/s），属于经验事实。虽然逻辑上内存碎片化确实会降低效率，但缺乏具体基准测试数据支持这些精确数值，且不同模型、不同实现（如 llama.cpp vs MLX）下表现差异巨大，直接断言具体数值缺乏普适性。 | 先验知识/题面给定，逻辑校验通过。内存碎片化导致可用显存减少进而降低吞吐符合计算机体系结构基本原理，但具体数值（10-20%）为经验估计，无外部来源直接支持，故降级为定性表述。
