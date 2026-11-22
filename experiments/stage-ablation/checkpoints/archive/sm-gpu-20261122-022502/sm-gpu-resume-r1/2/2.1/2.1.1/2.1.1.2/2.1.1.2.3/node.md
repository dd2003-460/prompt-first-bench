# N535: 性价比工作点 3（高成本低性）：RTX 5090 BF16 方案，Throughput = 33.2 tokens/s（BF16 权重 54GB，需 2 卡或 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

性价比工作点 3（高成本低性）：RTX 5090 BF16 方案，Throughput = 33.2 tokens/s（BF16 权重 54GB，需 2 卡或 offload），Quality_Score = 1.0，Cost = $3998（2x 5090），性价比 = (33.2 * 1.0) / 3998 ≈ 0.0083 tokens/s per $。

## Corrected Claim

性价比工作点 3（高成本低性）：RTX 5090 BF16 方案，Throughput = 33.2 tokens/s（BF16 权重 54GB，需 2 卡或 offload），Quality_Score = 1.0，Cost = $3998（2x 5090），性价比 = (33.2 * 1.0) / 3998 ≈ 0.0083 tokens/s per $。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 单卡显存 32GB，54GB 权重确实需 2 卡或 offload；2x 5090 成本约 $3998 符合市场定价；吞吐量 33.2 tokens/s 对于大模型在双卡 BF16 下的推理速度量级合理；性价比计算 (33.2 * 1.0) / 3998 ≈ 0.0083 数学正确。
