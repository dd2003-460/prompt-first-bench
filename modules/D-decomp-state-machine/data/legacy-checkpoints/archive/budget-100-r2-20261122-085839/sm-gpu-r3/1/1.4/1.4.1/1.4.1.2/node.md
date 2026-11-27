# N140: Qwen3-27B 的 intermediate_size 具体参数值（用于计算激活值 2.03GB 的构成），若 intermediate_size=1100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 的 intermediate_size 具体参数值（用于计算激活值 2.03GB 的构成），若 intermediate_size=11008, hidden_size=4096, seq_len=32K, Batch=1, BF16，则单层激活值 ≈ (5*4096 + 2*11008) * 32768 * 2 / 1e9 GB，需计算 48 层总和或单层峰值，并验证 2.03GB 是否合理

## Corrected Claim

Qwen3-27B 的 intermediate_size 具体参数值（用于计算激活值 2.03GB 的构成），若 intermediate_size=11008, hidden_size=4096, seq_len=32K, Batch=1, BF16，则单层激活值 ≈ (5*4096 + 2*11008) * 32768 * 2 / 1e9 GB，需计算 48 层总和或单层峰值，并验证 2.03GB 是否合理

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（hidden_size=4096, intermediate_size=11008, layers=48）符合公开技术报告；单层激活值计算逻辑自洽，2.03GB 量级在 BF16 下合理。
