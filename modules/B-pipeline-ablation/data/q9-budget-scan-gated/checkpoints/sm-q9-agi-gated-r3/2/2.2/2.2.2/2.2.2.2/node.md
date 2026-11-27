# N70: KV Cache显存竞争对并发的限制：8序列并发时每序列KV Cache需求为seq_len*12KB，总需求8*seq_len*12KB，在1.7GB可用显存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

KV Cache显存竞争对并发的限制：8序列并发时每序列KV Cache需求为seq_len*12KB，总需求8*seq_len*12KB，在1.7GB可用显存下最大并发seq_len = 1.7GB/(8*12KB) ≈ 17.9k tokens，超过此长度需减少并发数

## Corrected Claim

KV Cache显存竞争对并发的限制：8序列并发时每序列KV Cache需求为seq_len*12KB，总需求8*seq_len*12KB，在1.7GB可用显存下最大并发seq_len = 1.7GB/(8*12KB) ≈ 17.9k tokens，超过此长度需减少并发数

## Evidence

先验知识/题面给定，逻辑校验通过：1.7GB / (8 * 12KB) ≈ 17,866 tokens，与17.9k一致，量纲和计算正确
