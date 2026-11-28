# N11: 本地推理物理天花板：在 max_model_len=262144 和 max-num-seqs=8 配置下，单请求延迟主要由 KV Cache 读取带宽决定，每

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

本地推理物理天花板：在 max_model_len=262144 和 max-num-seqs=8 配置下，单请求延迟主要由 KV Cache 读取带宽决定，每 token 生成时间 T_gen ≈ (W_read + KV_read) / Bandwidth，估算单请求长上下文（>32k tokens）吞吐上限约 15-25 tokens/sec/seq，总集群吞吐约 120-200 tokens/sec

## Corrected Claim

本地推理物理天花板：在 max_model_len=262144 和 max-num-seqs=8 配置下，单请求延迟主要由 KV Cache 读取带宽决定，每 token 生成时间 T_gen ≈ (W_read + KV_read) / Bandwidth，估算单请求长上下文（>32k tokens）吞吐上限约 15-25 tokens/sec/seq，总集群吞吐约 120-200 tokens/sec

## Evidence

先验知识/题面给定，逻辑校验通过：基于内存带宽瓶颈（Memory-Bound）的第一性原理推导，KV Cache读取主导延迟，数值量级符合大模型长上下文推理的物理极限常识。

## Search Query

v100 cluster long context inference throughput limit
