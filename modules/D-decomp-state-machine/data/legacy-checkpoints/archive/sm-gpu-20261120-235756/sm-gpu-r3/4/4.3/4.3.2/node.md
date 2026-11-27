# N88: 32K 上下文下单个请求的 KV Cache 总显存占用：256 KB/token * 32,768 tokens = 8,388,608 KB ≈ 8.0 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

32K 上下文下单个请求的 KV Cache 总显存占用：256 KB/token * 32,768 tokens = 8,388,608 KB ≈ 8.0 GB（BF16 精度）。

## Corrected Claim

32K 上下文下单个请求的 KV Cache 总显存占用：256 KB/token * 32,768 tokens = 8,388,608 KB ≈ 8.0 GB（BF16 精度）。

## Evidence

先验知识/题面给定，逻辑校验通过：256 KB × 32,768 = 8,388,608 KB，换算为 GB 约为 8.0 GB，数值量级与计算逻辑自洽。
