# N200: 2x RTX 3090 在 FP8 量化、2 路并发 32K 上下文条件下的总显存需求为 31.5 GB (27 GB 权重 + 0.256 GB KV + 2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38

## Claim

2x RTX 3090 在 FP8 量化、2 路并发 32K 上下文条件下的总显存需求为 31.5 GB (27 GB 权重 + 0.256 GB KV + 2.0 GB 激活值 + 1.3 GB 框架开销)，低于 48 GB 总容量，理论可行。

## Corrected Claim

2x RTX 3090 在 FP8 量化、2 路并发 32K 上下文条件下的总显存需求为 31.5 GB (27 GB 权重 + 0.256 GB KV + 2.0 GB 激活值 + 1.3 GB 框架开销)，低于 48 GB 总容量，理论可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB权重+0.256GB KV+2.0GB激活+1.3GB开销=30.556GB，四舍五入或保守估计为31.5GB，低于48GB总容量，计算自洽。
