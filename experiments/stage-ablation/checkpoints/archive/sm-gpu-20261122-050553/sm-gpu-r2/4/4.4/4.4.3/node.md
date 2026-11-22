# N91: 1×A100 40GB 方案的显存容量限制：40GB 显存减去 27GB 权重后仅剩 13GB 用于 KV Cache，按 32K 上下文 BF16 KV Ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

1×A100 40GB 方案的显存容量限制：40GB 显存减去 27GB 权重后仅剩 13GB 用于 KV Cache，按 32K 上下文 BF16 KV Cache 需求 ~16GB 计算，存在 3GB 缺口，必须使用 FP8 KV Cache 或 INT8 量化 KV 才能运行，否则需限制上下文至 24K。

## Corrected Claim

1×A100 40GB 方案的显存容量限制：40GB 显存减去 27GB 权重后仅剩 13GB 用于 KV Cache，按 32K 上下文 BF16 KV Cache 需求 ~16GB 计算，存在 3GB 缺口，必须使用 FP8 KV Cache 或 INT8 量化 KV 才能运行，否则需限制上下文至 24K。

## Evidence

先验知识/题面给定，逻辑校验通过：40GB-27GB=13GB，13GB<16GB，缺口3GB，结论自洽。
