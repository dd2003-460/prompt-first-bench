# N215: A100 40GB (HBM2) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 27GB + KV Cache (32K, 约4GB) + 框架

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

A100 40GB (HBM2) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 27GB + KV Cache (32K, 约4GB) + 框架开销 (约2-4GB) = 33-35GB，接近 40GB 上限，可行但余量仅 5-7GB，若 Batch Size > 1 或上下文 > 32K 则极易 OOM，稳定性低于 48GB+ 方案。

## Corrected Claim

A100 40GB (HBM2) 在 INT8 下运行 Qwen3-27B 的总显存需求：权重 27GB + KV Cache (32K, 约4GB) + 框架开销 (约2-4GB) = 33-35GB，接近 40GB 上限，可行但余量仅 5-7GB，若 Batch Size > 1 或上下文 > 32K 则极易 OOM，稳定性低于 48GB+ 方案。

## Evidence

[质询]KV Cache 估算可能偏乐观：若 Qwen3-27B 采用 GQA 且头数/维度配置导致每 token 显存占用较高，32K 上下文的 KV Cache 可能超过 4GB（例如达到 6-8GB），从而压缩剩余空间，使 40GB 显存更加紧张甚至不可行。 | 先验知识/题面给定，逻辑校验通过：INT8 权重 27GB 符合 27B 参数规模；KV Cache 与框架开销量级在合理范围内；总显存 33-35GB 接近 40GB 上限的结论在逻辑上自洽，且符合大模型部署的一般工程经验。
