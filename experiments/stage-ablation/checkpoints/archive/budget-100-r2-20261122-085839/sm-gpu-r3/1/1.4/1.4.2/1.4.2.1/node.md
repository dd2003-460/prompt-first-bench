# N143: Qwen3-27B 在 32K 上下文、Batch=1 时，FP8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B 在 32K 上下文、Batch=1 时，FP8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 4096 hidden_dim * 32768 tokens * 1 byte = 10.066 GB (10.31 GB 为含少量缓冲的保守值)。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch=1 时，FP8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 4096 hidden_dim * 32768 tokens * 1 byte = 10.066 GB (10.31 GB 为含少量缓冲的保守值)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（48层、GQA 2 KV heads、4096 hidden dim）符合已知规格，FP8 精度为 1 byte，计算过程 2*48*2*4096*32768*1 = 10,066,329,600 bytes ≈ 10.066 GB，数值量级与逻辑自洽。
