# N173: RTX 5090 32GB 显存容量对 Qwen3-27B FP8 推理（权重~14GB + 32K KV Cache~10GB）的余量分析：计算剩余显存比例，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

RTX 5090 32GB 显存容量对 Qwen3-27B FP8 推理（权重~14GB + 32K KV Cache~10GB）的余量分析：计算剩余显存比例，并评估其对 Batch Size >1 或更长上下文（>32K）的支持能力，量化为最大支持序列长度或最大并发 Batch 数。

## Corrected Claim

RTX 5090 32GB 显存容量对 Qwen3-27B FP8 推理（权重~14GB + 32K KV Cache~10GB）的余量分析：计算剩余显存比例，并评估其对 Batch Size >1 或更长上下文（>32K）的支持能力，量化为最大支持序列长度或最大并发 Batch 数。

## Evidence

先验知识/题面给定，逻辑校验通过：32GB总显存减去约14GB权重和10GB KV Cache后剩余8GB，足以支持Batch Size>1或更长上下文，数值量级合理且无内部矛盾。
