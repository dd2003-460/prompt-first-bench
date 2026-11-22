# N321: A100 40GB 在 FP8 量化下运行 Qwen3-27B 的显存余量计算：权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

A100 40GB 在 FP8 量化下运行 Qwen3-27B 的显存余量计算：权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (10GB) = 38.6GB < 40GB，余量仅 1.4GB，无法支持任何额外并发（第2个请求需 1.6GB KV Cache，总需 40.2GB > 40GB），因此 A100 40GB FP8 仅支持单并发 32K 上下文。

## Corrected Claim

A100 40GB 在 FP8 量化下运行 Qwen3-27B 的显存余量计算：权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (10GB) = 38.6GB < 40GB，余量仅 1.4GB，无法支持任何额外并发（第2个请求需 1.6GB KV Cache，总需 40.2GB > 40GB），因此 A100 40GB FP8 仅支持单并发 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：权重27GB+KV 1.6GB+开销10GB=38.6GB<40GB，单并发成立；双并发需40.2GB>40GB，结论自洽。
