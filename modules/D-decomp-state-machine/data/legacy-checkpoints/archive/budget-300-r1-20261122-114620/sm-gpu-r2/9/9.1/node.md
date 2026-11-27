# N132: 并发数 N=4 时的 KV Cache 总占用量化：单请求 32K 上下文 KV Cache 为 1.6GB，4 并发总 KV Cache 为 6.4GB；加上

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

并发数 N=4 时的 KV Cache 总占用量化：单请求 32K 上下文 KV Cache 为 1.6GB，4 并发总 KV Cache 为 6.4GB；加上 BF16 权重 54GB 和框架开销 10GB，总显存需求为 70.4GB，单卡 RTX 4090 (24GB) 和 L40S (48GB) 均不可行，必须选择 A100 80GB 或 H100 80GB。

## Corrected Claim

并发数 N=4 时的 KV Cache 总占用量化：单请求 32K 上下文 KV Cache 为 1.6GB，4 并发总 KV Cache 为 6.4GB；加上 BF16 权重 54GB 和框架开销 10GB，总显存需求为 70.4GB，单卡 RTX 4090 (24GB) 和 L40S (48GB) 均不可行，必须选择 A100 80GB 或 H100 80GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 1.6GB*4=6.4GB，总显存 6.4+54+10=70.4GB，超过 24GB 和 48GB 显卡容量，结论符合硬件规格逻辑。
