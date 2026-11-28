# N14: 27B模型在V100集群上处理长上下文（>32k tokens）时，注意力机制的计算复杂度O(n^2)导致Prefill阶段延迟线性增长，单token生成延迟从

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

27B模型在V100集群上处理长上下文（>32k tokens）时，注意力机制的计算复杂度O(n^2)导致Prefill阶段延迟线性增长，单token生成延迟从<50ms（短上下文）增加到>200ms（256k上下文），成为科研长文档分析的主要瓶颈。

## Corrected Claim

27B模型在V100集群上处理长上下文（>32k tokens）时，Prefill阶段因注意力机制O(n^2)的计算复杂度导致延迟显著增加；同时，由于KV Cache占用大量显存，Decode阶段（单token生成）受限于显存带宽，延迟从<50ms（短上下文）增加到>200ms（256k上下文），成为科研长文档分析的主要瓶颈。

## Evidence

[质询]陈述中存在明显的逻辑/物理概念错误：注意力机制的计算复杂度 O(n^2) 通常指 Prefill 阶段的计算量随序列长度平方增长，但这并不直接导致 'Prefill 阶段延迟线性增长'（应为超线性/平方级增长，除非受限于内存带宽或其他瓶颈）；此外，'单 token 生成延迟'（Decode 阶段）从 <50ms 增加到 >200ms 虽然符合 KV Cache 增大导致的显存带宽压力增加的趋势，但将其归因于 '注意力机制的计算复杂度 O(n^2)' 是不准确的，因为 Decode 阶段的注意力计算复杂度是 O(n)（每步新 token 与所有历史 token 交互），主要瓶颈通常是显存带宽而非 FLOPs 的 O(n^2)。 | 先验知识/题面给定，逻辑校验发现归因错误：Prefill 延迟随 n^2 增长而非线性；Decode 延迟增加主要源于 KV Cache 显存访问开销（O(n) 计算复杂度），而非 O(n^2) 计算复杂度。

## Search Query

long context attention latency V100 256k tokens
