# N454: 12TB SMR HDD 的 5 年 TCO 中，硬件购置成本 C_hw_SMR = 34 * ¥1,300 (假设单价) = ¥44,200，相比 16TB 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N201

## Claim

12TB SMR HDD 的 5 年 TCO 中，硬件购置成本 C_hw_SMR = 34 * ¥1,300 (假设单价) = ¥44,200，相比 16TB CMR 方案（26 盘 * ¥1,450 = ¥37,700）高出 17%，但因其更高的单盘容量密度，每 TB 硬件成本略低，然而重建时间延长导致的 RTO 代价增量 ΔC_RTO_SMR 需单独计算。

## Corrected Claim

12TB SMR HDD 的 5 年 TCO 中，硬件购置成本 C_hw_SMR = 34 * ¥1,300 (假设单价) = ¥44,200，相比 16TB CMR 方案（26 盘 * ¥1,450 = ¥37,700）高出 17%，但因其更高的单盘容量密度，每 TB 硬件成本略低，然而重建时间延长导致的 RTO 代价增量 ΔC_RTO_SMR 需单独计算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（44200 vs 37700，差值约17.2%），单位换算与TCO构成逻辑自洽。
