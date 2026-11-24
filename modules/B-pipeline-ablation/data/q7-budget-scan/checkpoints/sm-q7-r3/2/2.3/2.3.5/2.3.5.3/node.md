# N218: Intelligent-Tiering 监控费与存储费的占比敏感性：若温数据 100TB 中 50% 被判定为 Infrequent Access（单价 $0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Intelligent-Tiering 监控费与存储费的占比敏感性：若温数据 100TB 中 50% 被判定为 Infrequent Access（单价 $0.0125/GB/月），存储费 = 50,000*$0.023 + 50,000*$0.0125 = $1,775/月，监控费 = 100,000*$0.0025 = $250/月，监控费占比 = 250/1775 ≈ 14.1%，高于 N70 假设的 6%，需修正 TCO 模型。

## Corrected Claim

Intelligent-Tiering 监控费与存储费的占比敏感性：若温数据 100TB 中 50% 被判定为 Infrequent Access（单价 $0.0125/GB/月），存储费 = 50,000*$0.023 + 50,000*$0.0125 = $1,775/月，监控费 = 100,000*$0.0025 = $250/月，监控费占比 = 250/1775 ≈ 14.1%，高于 N70 假设的 6%，需修正 TCO 模型。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 50000*0.023 + 50000*0.0125 = 1150 + 625 = 1775，监控费 100000*0.0025 = 250，占比 250/1775 ≈ 14.08%，数值与逻辑均自洽。
