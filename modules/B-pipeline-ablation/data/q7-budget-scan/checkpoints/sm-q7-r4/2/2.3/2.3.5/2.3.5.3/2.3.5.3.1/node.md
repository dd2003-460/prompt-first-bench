# N615: 监控费与存储费占比计算公式：Ratio = Cost_monitoring / (Cost_monitoring + Cost_storage)；其中 Cost

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N218

## Claim

监控费与存储费占比计算公式：Ratio = Cost_monitoring / (Cost_monitoring + Cost_storage)；其中 Cost_storage = Σ(各层级数据量 * 各层级单价)；若温数据 100TB 中 50% 为 Frequent Access（$0.023/GB/月）、50% 为 Infrequent Access（$0.0125/GB/月），则 Cost_storage = 50,000 * 0.023 + 50,000 * 0.0125 = $1,775/月，Cost_monitoring = 100,000 * 0.0025 = $250/月，Ratio = 250 / (250 + 1775) ≈ 12.3%（非 14.1%，因分母需包含监控费）。

## Corrected Claim

监控费与存储费占比计算公式：Ratio = Cost_monitoring / (Cost_monitoring + Cost_storage)；其中 Cost_storage = Σ(各层级数据量 * 各层级单价)；若温数据 100TB 中 50% 为 Frequent Access（$0.023/GB/月）、50% 为 Infrequent Access（$0.0125/GB/月），则 Cost_storage = 50,000 * 0.023 + 50,000 * 0.0125 = $1,775/月，Cost_monitoring = 100,000 * 0.0025 = $250/月，Ratio = 250 / (250 + 1775) ≈ 12.3%（非 14.1%，因分母需包含监控费）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（50000*0.023=1150, 50000*0.0125=625, Sum=1775; 100000*0.0025=250; 250/(250+1775)=250/2025≈12.34%），公式定义与计算过程自洽。
