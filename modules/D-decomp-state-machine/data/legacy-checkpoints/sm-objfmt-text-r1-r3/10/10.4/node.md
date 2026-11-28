# N82: 显存容量对最大并发 Batch Size 的限制：RTX 4090 (24GB) 在 32K 上下文下最大并发约为 1-2 请求，A100 80GB 约为 4-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

显存容量对最大并发 Batch Size 的限制：RTX 4090 (24GB) 在 32K 上下文下最大并发约为 1-2 请求，A100 80GB 约为 4-6 请求，H100 80GB 约为 4-6 请求，这是多用户场景下 TCO 差异的关键约束。

## Corrected Claim

显存容量对最大并发 Batch Size 的限制：RTX 4090 (24GB) 在 32K 上下文下最大并发约为 1-2 请求，A100 80GB 约为 4-6 请求，H100 80GB 约为 4-6 请求，这是多用户场景下 TCO 差异的关键约束。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Transformer推理显存占用估算（KV Cache主导），24GB显存难以支撑32K长上下文的并发，而80GB显存可支撑少量并发，数量级符合工程常识。
