# N259: Apple M3 Ultra 在 32K 上下文下的吞吐量衰减因子：由于 M3 Ultra 统一内存带宽 (800GB/s) 低于 RTX 4090 (1000

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

Apple M3 Ultra 在 32K 上下文下的吞吐量衰减因子：由于 M3 Ultra 统一内存带宽 (800GB/s) 低于 RTX 4090 (1000GB/s) 且无专用显存，长上下文 KV Cache 占用增加导致有效带宽下降，实测吞吐量较短上下文 (2K) 下降约 15-25%，即 32K 上下文下吞吐量约为 20-30 tokens/s。

## Corrected Claim

Apple M3 Ultra 在 32K 上下文下的吞吐量通常低于短上下文 (2K) 场景，主要受限于统一内存带宽 (800GB/s) 及 KV Cache 占用增加导致的带宽压力，具体吞吐量取决于模型规模与量化方式。

## Evidence

[质询]吞吐量具体数值（20-30 tokens/s）及衰减比例（15-25%）高度依赖于具体的模型规模（如7B, 13B, 70B）、量化精度（FP16, INT8, INT4）以及推理框架优化，缺乏这些关键变量使得该具体数值缺乏普适性，属于过度具体的经验断言。 | 先验知识/题面给定，逻辑校验通过：M3 Ultra带宽(800GB/s)确实低于RTX 4090(1000GB/s)，长上下文KV Cache增加导致带宽瓶颈是合理机制，但具体吞吐量数值因模型而异，无法从第一性原理唯一确定，故降级为定性表述。
