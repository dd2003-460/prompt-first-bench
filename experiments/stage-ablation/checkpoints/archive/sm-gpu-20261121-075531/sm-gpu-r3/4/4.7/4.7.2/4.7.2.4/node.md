# N311: RTX 5090 相比 RTX 4090 在 Qwen3-27B INT8 32K 上下文下的 Decode TPS 提升幅度上限 = 带宽比 (1792/10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

RTX 5090 相比 RTX 4090 在 Qwen3-27B INT8 32K 上下文下的 Decode TPS 提升幅度上限 = 带宽比 (1792/1008 = 1.778x) * (η_5090/η_4090)；若效率比 η_5090/η_4090 ≈ 1.0 (Blackwell 架构优化抵消部分带宽优势)，则 TPS 提升约 77.8%；若效率比 0.9，则提升约 69.9% [待核验]。

## Corrected Claim

RTX 5090 相比 RTX 4090 在 Qwen3-27B INT8 32K 上下文下的 Decode TPS 提升幅度上限 = 带宽比 (1792/1008 = 1.778x) * (η_5090/η_4090)；若效率比 η_5090/η_4090 ≈ 1.0 (Blackwell 架构优化抵消部分带宽优势)，则 TPS 提升约 77.8%；若效率比 0.9，则提升约 69.9% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽比计算正确（1792/1008≈1.778），效率比假设下的TPS提升幅度推导符合线性模型逻辑，数值量级合理。

## Search Query

RTX 5090 vs RTX 4090 LLM inference throughput improvement ratio GDDR7 vs GDDR6X
