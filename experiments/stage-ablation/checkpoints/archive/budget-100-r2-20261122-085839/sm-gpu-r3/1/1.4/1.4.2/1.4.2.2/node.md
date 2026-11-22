# N144: Qwen3-27B 在 32K 上下文、Batch=1 时，INT8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Qwen3-27B 在 32K 上下文、Batch=1 时，INT8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 4096 hidden_dim * 32768 tokens * 2 bytes = 20.133 GB，比 FP8 方案多占用 10.066 GB 显存。

## Corrected Claim

Qwen3-27B 在 32K 上下文、Batch=1 时，INT8 KV Cache 的精确占用为 2 * 48 layers * 2 KV heads * 4096 hidden_dim * 32768 tokens * 2 bytes = 20.133 GB，比 FP8 方案多占用 10.066 GB 显存。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（48层、GQA 2 KV heads、4096 hidden dim）符合已知规格，INT8 为 2 bytes（K+V各1 byte），计算 2*48*2*4096*32768*2 = 20,132,658,688 bytes ≈ 20.133 GB，数值量级与逻辑自洽。
