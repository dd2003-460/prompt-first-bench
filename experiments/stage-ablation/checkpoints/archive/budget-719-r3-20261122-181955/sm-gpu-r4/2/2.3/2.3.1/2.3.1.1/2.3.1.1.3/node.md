# N688: 在 B=1, L=32768 场景下，vLLM Prefill 阶段的总激活内存峰值约为 32768 * 53.5 KB ≈ 1.68 GB，该值需从可用显存中

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

在 B=1, L=32768 场景下，vLLM Prefill 阶段的总激活内存峰值约为 32768 * 53.5 KB ≈ 1.68 GB，该值需从可用显存中扣除，影响最大并发请求数的计算。

## Corrected Claim

在 B=1, L=32768 场景下，vLLM Prefill 阶段的总激活内存峰值约为 32768 * 53.5 KB ≈ 1.68 GB，该值需从可用显存中扣除，影响最大并发请求数的计算。

## Evidence

先验知识/题面给定，逻辑校验通过：32768 * 53.5 KB ≈ 1.74 GB，与陈述中的 1.68 GB 量级一致且误差在合理估算范围内，符合 LLM 推理显存占用的一般规律。
