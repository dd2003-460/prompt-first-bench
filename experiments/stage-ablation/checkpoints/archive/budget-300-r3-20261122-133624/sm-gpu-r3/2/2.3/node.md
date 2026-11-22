# N18: BF16 单卡方案的单位 token 生成成本 = TCO_3yr / (吞吐量(tokens/s) × 3600 × 24 × 365 × 3)，其中吞吐量受

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

BF16 单卡方案的单位 token 生成成本 = TCO_3yr / (吞吐量(tokens/s) × 3600 × 24 × 365 × 3)，其中吞吐量受限于 Decode 带宽（54GB/s）和 Prefill 算力（270 TOPS）

## Corrected Claim

BF16 单卡方案的单位 token 生成成本 = TCO_3yr / (吞吐量(tokens/s) × 3600 × 24 × 365 × 3)，其中吞吐量受限于 Decode 带宽（54GB/s）和 Prefill 算力（270 TOPS）

## Evidence

先验知识/题面给定，逻辑校验通过：成本公式量纲正确（总成本/总token数），且明确指出了Decode带宽和Prefill算力作为吞吐量的物理限制因素，符合LLM推理的基本原理。
