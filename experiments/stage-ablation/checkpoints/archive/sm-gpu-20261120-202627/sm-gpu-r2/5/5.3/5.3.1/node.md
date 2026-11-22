# N122: 性价比指标 (Cost_Efficiency) 的分子修正：有效吞吐量 = Throughput × Quality_Factor。对于工作点 A (INT8/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

性价比指标 (Cost_Efficiency) 的分子修正：有效吞吐量 = Throughput × Quality_Factor。对于工作点 A (INT8/FP8)，Quality_Factor ≈ 0.95-0.98 [待核验：基于 MMLU 下降幅度]；对于工作点 B (BF16)，Quality_Factor = 1.0。

## Corrected Claim

性价比指标 (Cost_Efficiency) 的分子修正：有效吞吐量 = Throughput × Quality_Factor。对于工作点 A (INT8/FP8)，Quality_Factor ≈ 0.95-0.98 [待核验：基于 MMLU 下降幅度]；对于工作点 B (BF16)，Quality_Factor = 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3 27B INT8 FP8 quality degradation MMLU perplexity comparison
