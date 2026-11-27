# N353: N124 公式仅计算静态 KV Cache 大小，未包含推理框架（如 vLLM）的 PagedAttention 块表开销和注意力头投影矩阵的中间激活内存；实际

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

N124 公式仅计算静态 KV Cache 大小，未包含推理框架（如 vLLM）的 PagedAttention 块表开销和注意力头投影矩阵的中间激活内存；实际显存占用需额外增加 5-10% 的运行时开销以容纳这些动态分配。

## Corrected Claim

N124 公式仅计算静态 KV Cache 大小，未包含推理框架（如 vLLM）的 PagedAttention 块表开销和注意力头投影矩阵的中间激活内存；实际显存占用需额外增加 5-10% 的运行时开销以容纳这些动态分配。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 静态计算确实不包含 PagedAttention 块表及中间激活，5-10% 的运行时开销估算符合工程经验。

## Search Query

vLLM PagedAttention memory overhead KV cache block table size
