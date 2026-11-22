# N57: A100 80GB (2039 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

A100 80GB (2039 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐：Bytes_per_token ≈ 27.1 GB (权重主导)，Throughput_max ≈ 2039 / 27.1 ≈ 75.2 tokens/s [待核验: 实际带宽利用率通常为 60-70%，有效吞吐约 45-52 tokens/s]

## Corrected Claim

A100 80GB (2039 GB/s) 在 Batch=1, INT8 权重, BF16 KV Cache, 32K 上下文下的 Decode 理论上限吞吐：Bytes_per_token ≈ 27.1 GB (权重主导)，Throughput_max ≈ 2039 / 27.1 ≈ 75.2 tokens/s [待核验: 实际带宽利用率通常为 60-70%，有效吞吐约 45-52 tokens/s]

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 显存带宽 2039 GB/s 为已知规格；Decode 阶段每 token 需读取全部权重（INT8 下约 27.1 GB，对应约 27B 参数模型），理论上限 2039/27.1 ≈ 75.2 tokens/s 计算正确；实际带宽利用率 60-70% 符合工程经验，有效吞吐 45-52 tokens/s 合理。
