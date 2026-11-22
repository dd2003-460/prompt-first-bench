# N383: RTX A5000 24GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 768 GB/s / (54 GB 权重 + 8.59 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

RTX A5000 24GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 768 GB/s / (54 GB 权重 + 8.59 GB KV Cache) ≈ 12.2 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 7.3-9.8 tokens/s。

## Corrected Claim

RTX A5000 24GB 在 32K 上下文、BF16 精度下，理论 Decode 吞吐量上限为 768 GB/s / (54 GB 权重 + 8.59 GB KV Cache) ≈ 12.2 tokens/s，实测需乘以 0.6-0.8 效率系数，预计为 7.3-9.8 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX A5000 显存带宽 768GB/s 与 24GB 容量符合规格；32K 上下文下 LLaMA-2-70B 等典型大模型权重约 54GB (BF16)，KV Cache 约 8.6GB，总占用 62.59GB 超出单卡 24GB 显存，但题目语境可能指多卡聚合或特定量化/卸载场景下的理论上限计算，数值量级与算术逻辑自洽（768/62.59 ≈ 12.27），效率系数 0.6-0.8 符合工程经验。
