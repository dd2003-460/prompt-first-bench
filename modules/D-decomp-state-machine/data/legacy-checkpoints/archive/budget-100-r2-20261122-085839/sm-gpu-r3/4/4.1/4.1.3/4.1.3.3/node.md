# N200: H100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

H100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth / Bytes_per_token) * 1000。代入数值：(2847.5 GB/s / 27.104 GB) * 1000 ≈ 105.06 tokens/s。

## Corrected Claim

H100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth / Bytes_per_token) * 1000。代入数值：(2847.5 GB/s / 27.104 GB) * 1000 ≈ 105.06 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 HBM3 带宽约 3.35TB/s，有效带宽 2847.5GB/s 合理；27.104GB 权重对应约 27B 参数模型（INT8 下 1字节/参数），计算 (2847.5/27.104)*1000 ≈ 105.06 tokens/s 数学正确且符合大模型推理带宽瓶颈理论。
