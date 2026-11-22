# N698: 带宽效率差异对 Decode 速度的实际影响需修正：5090 的 GDDR7 访问延迟略高于 GDDR6X，且驱动优化成熟度较低，实际 Decode 吞吐量提升

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N288

## Claim

带宽效率差异对 Decode 速度的实际影响需修正：5090 的 GDDR7 访问延迟略高于 GDDR6X，且驱动优化成熟度较低，实际 Decode 吞吐量提升幅度可能低于带宽比 (1792/1008 = 1.78x)，预计实际性能提升为 1.5x-1.6x。

## Corrected Claim

带宽效率差异对 Decode 速度的实际影响需修正：5090 的 GDDR7 访问延迟及驱动优化成熟度可能影响实际性能，实际 Decode 吞吐量提升幅度可能低于带宽比 (1.78x)，预计实际性能提升低于 1.78x。

## Evidence

[质询]该陈述包含具体的经验性预测数值（1.5x-1.6x）和特定硬件的微观行为断言（GDDR7延迟略高于GDDR6X、驱动成熟度低），这些属于经验事实，无法从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 vs 4090 LLM inference benchmark decode tokens per second
