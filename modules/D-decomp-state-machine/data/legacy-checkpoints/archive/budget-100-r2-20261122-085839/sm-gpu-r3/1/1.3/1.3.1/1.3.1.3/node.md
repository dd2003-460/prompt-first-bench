# N133: 推理框架（如 vLLM/llama.cpp）在 Decode 阶段采用 PagedAttention 或类似机制时，激活值显存是否仅为当前正在计算的单层大小（即

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

推理框架（如 vLLM/llama.cpp）在 Decode 阶段采用 PagedAttention 或类似机制时，激活值显存是否仅为当前正在计算的单层大小（即 O(1) 层数），还是需保留全模型所有层的激活值（O(48) 层数），这决定了总激活值显存是单层计算值的 1 倍还是 48 倍

## Corrected Claim

在标准 Decode 阶段，由于自回归生成的特性，激活值显存通常仅需保留当前计算层或极少层的数据（O(1) 量级），而非全模型所有层（O(48)）。PagedAttention 主要优化的是 KV Cache 的显存管理，而非直接决定激活值显存的层数复杂度。

## Evidence

[质询]该陈述混淆了「KV Cache 显存」与「激活值（Activations）显存」的概念。PagedAttention 主要优化的是 KV Cache 的碎片化问题，其显存占用与序列长度和层数成正比（O(L)），而非 O(1)。对于激活值，在 Decode 阶段（自回归生成），由于是逐 token 生成，通常不需要保留所有层的中间激活值用于反向传播（除非是投机解码或特定训练场景），因此激活值显存确实接近 O(1) 层数（仅当前层或少数层），但这并非 PagedAttention 的直接结果，而是 Decode 阶段计算图特性的结果。若将 PagedAttention 归因为激活值显存 O(1) 的原因，属于因果归因错误。 | 无可用外部证据。逻辑上，Decode 阶段激活值显存确实远小于 Prefill 阶段，但 PagedAttention 针对的是 KV Cache 而非激活值。陈述将 PagedAttention 与激活值显存 O(1) 直接挂钩存在概念混淆，但结论（激活值显存非 O(48) 全层保留）在标准推理场景下大致成立，故降级为定性表述。

## Search Query

vLLM paged attention activation memory footprint single layer vs all layers
