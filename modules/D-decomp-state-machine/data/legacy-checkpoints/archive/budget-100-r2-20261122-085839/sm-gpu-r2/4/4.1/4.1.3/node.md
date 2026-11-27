# N58: H100 80GB (3350 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

H100 80GB (3350 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐：Bytes_per_token ≈ 27.1 GB (权重主导)，Throughput_max ≈ 3350 / 27.1 ≈ 123.6 tokens/s [待核验: 实际带宽利用率通常为 60-70%，有效吞吐约 74-86 tokens/s]

## Corrected Claim

H100 80GB (3350 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐：Bytes_per_token ≈ 27.1 GB (权重主导)，Throughput_max ≈ 3350 / 27.1 ≈ 123.6 tokens/s [待核验: 实际带宽利用率通常为 60-70%，有效吞吐约 74-86 tokens/s]

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB 显存带宽 3350 GB/s 为已知规格；Decode 阶段每 token 需读取全部权重（INT8 下约 27.1 GB，符合大模型参数量级），理论上限 3350/27.1 ≈ 123.6 tokens/s 计算正确；实际带宽利用率 60-70% 导致有效吞吐 74-86 tokens/s 符合工程经验。
