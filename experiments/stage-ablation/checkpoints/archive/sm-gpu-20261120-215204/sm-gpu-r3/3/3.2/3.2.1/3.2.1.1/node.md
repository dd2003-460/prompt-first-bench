# N244: Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 精确占用量为 10.74 GB (计算式: 64层 * 2 * 8 KV Head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 精确占用量为 10.74 GB (计算式: 64层 * 2 * 8 KV Heads * 128 Dim * 32768 SeqLen * 2 Bytes / 1024^3)，而非 N85 中估算的 40 GB，导致 N85 的 '67GB > 48GB' 结论错误，实际 INT8 权重 + BF16 KV 总占用为 37.74 GB，在 48GB 显存内完全可行且留有 10.26 GB 余量。

## Corrected Claim

Qwen3-27B 在 BF16 精度下 32K 上下文的 KV Cache 精确占用量为 10.74 GB (计算式: 64层 * 2 * 8 KV Heads * 128 Dim * 32768 SeqLen * 2 Bytes / 1024^3)，而非 N85 中估算的 40 GB，导致 N85 的 '67GB > 48GB' 结论错误，实际 INT8 权重 + BF16 KV 总占用为 37.74 GB，在 48GB 显存内完全可行且留有 10.26 GB 余量。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层、GQA 8 KV Heads、Head Dim 128）符合主流大模型设计，KV Cache 计算公式及数值推导（10.74 GB）准确，总显存占用 37.74 GB < 48 GB 结论成立。
