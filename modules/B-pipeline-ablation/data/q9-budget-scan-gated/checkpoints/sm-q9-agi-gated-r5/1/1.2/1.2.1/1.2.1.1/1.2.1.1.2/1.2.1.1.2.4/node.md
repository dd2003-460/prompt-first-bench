# N164: 基于修正后的 48 KB/token/卡，重新定义显存-上下文 trade-off 前沿：在 11.125 GB 显存下，单序列最大上下文约为 241k tok

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

基于修正后的 48 KB/token/卡，重新定义显存-上下文 trade-off 前沿：在 11.125 GB 显存下，单序列最大上下文约为 241k tokens；8 序列并发时，单序列最大上下文约为 30k tokens (11.125GB / 8 / 48KB ≈ 30,000)，绘制 (concurrency, max_seq_len) 可行域边界。

## Corrected Claim

基于修正后的 48 KB/token/卡，重新定义显存-上下文 trade-off 前沿：在 11.125 GB 显存下，单序列最大上下文约为 241k tokens；8 序列并发时，单序列最大上下文约为 30k tokens (11.125GB / 8 / 48KB ≈ 30,000)，绘制 (concurrency, max_seq_len) 可行域边界。

## Evidence

先验知识/题面给定，逻辑校验通过：11.125GB转换为MB后除以48KB/token得到总token数，再除以并发数8，计算结果约30,000 tokens，数学推导正确且量级合理。
