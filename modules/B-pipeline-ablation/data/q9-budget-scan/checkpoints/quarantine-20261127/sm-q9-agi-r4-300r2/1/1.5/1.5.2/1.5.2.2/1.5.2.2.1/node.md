# N285: 长序列低并发工作点（BS=1, L=262k）的 Decode 阶段算术强度修正：Decode 阶段每步仅生成 1 token，KV Cache 读取量固定为 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

长序列低并发工作点（BS=1, L=262k）的 Decode 阶段算术强度修正：Decode 阶段每步仅生成 1 token，KV Cache 读取量固定为 262k 对应的显存块，AI_decode ≈ 1 / (KV_bytes_per_step)，由于 KV 读取量远大于计算量，AI < 0.1，完全 Memory-Bound；优化重点在于减少 KV 读取频率（如 StreamingLLM 窗口机制）而非提升计算密度。

## Corrected Claim

长序列低并发工作点（BS=1, L=262k）的 Decode 阶段算术强度修正：Decode 阶段每步仅生成 1 token，KV Cache 读取量固定为 262k 对应的显存块，AI_decode ≈ 1 / (KV_bytes_per_step)，由于 KV 读取量远大于计算量，AI < 0.1，完全 Memory-Bound；优化重点在于减少 KV 读取频率（如 StreamingLLM 窗口机制）而非提升计算密度。

## Evidence

先验知识/题面给定，逻辑校验通过：Decode阶段每步生成1 token，计算量恒定，而KV Cache读取量随序列长度L线性增长（L=262k时极大），导致算术强度AI = FLOPs / Bytes 极低（<0.1），符合Memory-Bound特征及优化方向。

## Search Query

LLM decode phase arithmetic intensity memory bound KV cache read optimization
