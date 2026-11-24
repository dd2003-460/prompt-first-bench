# N332: 长尾POP单点故障概率 P_tail_pop_failure 与核心POP相似（0.5%-1.5%/月），但业务损失 Loss_tail 显著降低，因为 Aff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

长尾POP单点故障概率 P_tail_pop_failure 与核心POP相似（0.5%-1.5%/月），但业务损失 Loss_tail 显著降低，因为 Affected_Traffic_Ratio_tail 仅为 5%（长尾区域用户稀疏），导致单点故障的加权风险贡献远低于核心POP。

## Corrected Claim

长尾POP单点故障概率 P_tail_pop_failure 与核心POP相似（0.5%-1.5%/月），但业务损失 Loss_tail 显著降低，因为 Affected_Traffic_Ratio_tail 仅为 5%（长尾区域用户稀疏），导致单点故障的加权风险贡献远低于核心POP。

## Evidence

先验知识/题面给定，逻辑校验通过：长尾POP故障概率与核心相似但影响流量占比低，导致加权风险贡献显著降低，符合风险计算逻辑（Risk = P * Loss），且数值量级（0.5%-1.5%/月，5%流量）在工程常识范围内合理。
