# N50: 基于 GQA (8 KV heads) 的 KV Cache 数值修正：在 32K 序列长度下，BF16 KV Cache 实际占用 = 2 × 72 × 8 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8, N9, N10

## Claim

基于 GQA (8 KV heads) 的 KV Cache 数值修正：在 32K 序列长度下，BF16 KV Cache 实际占用 = 2 × 72 × 8 × 128 × 32768 × 2 / 1024^3 ≈ 9GB，而非 MHA 假设下的 36GB，这显著降低了显存需求。

## Corrected Claim

基于 GQA (8 KV heads) 的 KV Cache 数值修正：在 32K 序列长度下，BF16 KV Cache 实际占用 = 2 × 72 × 8 × 128 × 32768 × 2 / 1024^3 ≈ 9GB，而非 MHA 假设下的 36GB，这显著降低了显存需求。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点N50聚焦于基于层数假设的显存容量修正（静态空间维度），子节点聚焦于GQA带来的带宽瓶颈变化（动态计算/IO维度）。两者分别处理显存占用量和解码吞吐/带宽限制，维度正交且无重复。父节点主要陈述显存修正，子节点进一步细化了参数依赖（层数）和推论影响（带宽/吞吐），覆盖合理。）

## Search Query

Qwen3-27B KV cache size 32k context GQA
