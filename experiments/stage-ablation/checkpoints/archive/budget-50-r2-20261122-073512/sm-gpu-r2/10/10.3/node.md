# N196: INT4 量化方案在 2 路并发 32K 上下文下的总显存需求为 17.1 GB (13.5 GB 权重 + 0.256 GB KV + 2.0 GB 激活值 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38

## Claim

INT4 量化方案在 2 路并发 32K 上下文下的总显存需求为 17.1 GB (13.5 GB 权重 + 0.256 GB KV + 2.0 GB 激活值 + 1.3 GB 框架开销)，低于 RTX 4090 的 24 GB 容量，理论可行。

## Corrected Claim

INT4 量化方案在 2 路并发 32K 上下文下的总显存需求为 17.1 GB (13.5 GB 权重 + 0.256 GB KV + 2.0 GB 激活值 + 1.3 GB 框架开销)，低于 RTX 4090 的 24 GB 容量，理论可行。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+0.256+2.0+1.3=17.056≈17.1 GB，且17.1 < 24 GB，数值量级与算术逻辑自洽。
