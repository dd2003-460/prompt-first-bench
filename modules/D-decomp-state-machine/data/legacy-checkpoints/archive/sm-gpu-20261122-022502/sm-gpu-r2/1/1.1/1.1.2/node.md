# N34: Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~0.2GB) 和激活值/临时缓冲区 (~1-2GB)，总显存需求下限为 55.2GB，因此32GB显存GPU在BF16下缺口为 23.2GB

## Corrected Claim

Qwen3-27B BF16权重文件大小为 54GB (27,000,000,000 params * 2 bytes/param)，加上KV Cache (~0.2GB) 和激活值/临时缓冲区 (~1-2GB)，总显存需求下限为 55.2GB，因此32GB显存GPU在BF16下缺口为 23.2GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重确为54GB，加上KV Cache和激活值后总显存需求远超32GB，缺口计算正确。
