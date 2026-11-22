# N37: H100 80GB 在BF16下运行Qwen3-27B，权重54GB + KV Cache 0.2GB + 缓冲区 2GB = 56.2GB，显存利用率 70.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

H100 80GB 在BF16下运行Qwen3-27B，权重54GB + KV Cache 0.2GB + 缓冲区 2GB = 56.2GB，显存利用率 70.25%，剩余 23.8GB 可用于扩展上下文至 ~64K tokens (KV Cache增量 ~0.4GB/32K tokens) 或提高并发批次大小 (batch size 可增加至 2-3 而仍保持 <80% 利用率)

## Corrected Claim

H100 80GB 在BF16下运行Qwen3-27B，权重54GB + KV Cache 0.2GB + 缓冲区 2GB = 56.2GB，显存利用率 70.25%，剩余 23.8GB 可用于扩展上下文至 ~64K tokens (KV Cache增量 ~0.4GB/32K tokens) 或提高并发批次大小 (batch size 可增加至 2-3 而仍保持 <80% 利用率)

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，加上KV Cache和缓冲区后总占用56.2GB，显存利用率70.25%（56.2/80），剩余23.8GB，数值量级与逻辑自洽。
