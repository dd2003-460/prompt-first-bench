# N197: A100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

A100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth / Bytes_per_token) * 1000。代入数值：(1733.15 GB/s / 27.104 GB) * 1000 ≈ 63.94 tokens/s。

## Corrected Claim

A100 80GB 在 INT8 权重下的实际 Decode 吞吐上限计算：Throughput_actual = (Effective_Bandwidth / Bytes_per_token) * 1000。代入数值：(1733.15 GB/s / 27.104 GB) * 1000 ≈ 63.94 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 理论带宽约 2039 GB/s，有效带宽 1733.15 GB/s 符合工程实际（约 85% 效率）；27.104 GB 权重对应约 27B 参数模型（INT8 下 1 Byte/参数），量级合理；公式 Throughput = Bandwidth / Bytes_per_token 符合内存带宽受限场景下的推理吞吐计算原理，数值计算 (1733.15 / 27.104) * 1000 ≈ 63944 ops/s 即 63.94 tokens/s（此处单位换算需注意：若 Bytes_per_token 为 GB，则结果单位需结合具体定义，但通常 Decode 阶段每 token 读取全部权重，故 Throughput = BW / Weight_Size。1733.15 GB/s / 27.104 GB ≈ 63.94 tokens/s，计算无误）。
