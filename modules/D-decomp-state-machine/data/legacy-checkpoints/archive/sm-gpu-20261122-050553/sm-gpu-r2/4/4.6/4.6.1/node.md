# N95: 在 24GB 显存约束下，Qwen3-27B 唯一可行的量化精度为 W4 (4-bit)，其显存占用计算为：权重 27B * 0.5 bytes = 13.5G

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

在 24GB 显存约束下，Qwen3-27B 唯一可行的量化精度为 W4 (4-bit)，其显存占用计算为：权重 27B * 0.5 bytes = 13.5GB + KV Cache (32K ctx, BF16) ≈ 16GB = 29.5GB > 24GB，结论是即使 W4 也超出 24GB 限制，必须启用 PagedAttention 或降低上下文至 ~16K 才能单卡运行。

## Corrected Claim

在 24GB 显存约束下，Qwen3-27B 采用 W4 量化后权重占用约 13.5GB。若 KV Cache 估算准确（32K ctx 下通常 < 4GB），总显存占用约 17-18GB，理论上可在 24GB 显存单卡运行，无需强制降低上下文至 16K 或启用 PagedAttention（除非 Batch Size 较大或上下文极长）。

## Evidence

[质询]KV Cache 估算严重失实：对于 27B 参数量的模型（假设层数~40-60，KV头数~8-16），32K 上下文的 KV Cache 占用通常在 1-4GB 左右（取决于具体架构如 GQA/MQA），而非 16GB。16GB 的估算可能混淆了 Batch Size 或使用了错误的公式（如误将全注意力矩阵当作 KV Cache），导致总显存占用被高估，从而得出“必须降低上下文”的错误结论。实际上 W4 量化后权重约 13.5GB，加上合理的 KV Cache 和激活值，24GB 显存通常足以支持 32K 上下文（甚至更高），无需强制降低至 16K。 | 先验知识/题面给定，逻辑校验未通过：KV Cache 数值量级错误（32K ctx 下 27B 模型 KV Cache 远小于 16GB），导致总显存计算错误，结论不可靠。
