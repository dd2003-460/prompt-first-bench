# N17: 有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_Original 为无更新时的 LRU 字节命中率（来自子问 a 的结果），P_invalid 来自 N6。

## Corrected Claim

有效命中率折损因子 Discount_Factor = 1 - P_invalid * (1 - Hit_Rate_Original)，其中 Hit_Rate_Original 为无更新时的 LRU 字节命中率（来自子问 a 的结果），P_invalid 来自 N6。

## Evidence

父节点级核验通过：正交+完备+无冗余（父节点定义了计算公式及其参数来源，子节点执行了具体的数值代入与计算。由于只有一个子节点，不存在正交性冲突或冗余问题。子节点涵盖了父节点公式应用的最终步骤，且参数来源（P_invalid, Hit_Rate_Original）在父节点中已明确界定，因此分解是完备的。）
