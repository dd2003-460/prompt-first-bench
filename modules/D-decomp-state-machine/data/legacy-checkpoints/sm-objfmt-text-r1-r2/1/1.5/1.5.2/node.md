# N38: RTX 4090 在 BF16 精度下的理论最大 Decode 吞吐率 = 1008 GB/s / 54 GB ≈ 18.67 Tokens/s；在 FP8 精

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

RTX 4090 在 BF16 精度下的理论最大 Decode 吞吐率 = 1008 GB/s / 54 GB ≈ 18.67 Tokens/s；在 FP8 精度下为 1008 GB/s / 27 GB ≈ 37.33 Tokens/s。

## Corrected Claim

RTX 4090 在 BF16 精度下的理论最大 Decode 吞吐率 = 1008 GB/s / 54 GB ≈ 18.67 Tokens/s；在 FP8 精度下为 1008 GB/s / 27 GB ≈ 37.33 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽约1008GB/s，LLM Decode阶段受限于内存带宽，吞吐量=带宽/模型大小，计算逻辑自洽且数值量级合理。
