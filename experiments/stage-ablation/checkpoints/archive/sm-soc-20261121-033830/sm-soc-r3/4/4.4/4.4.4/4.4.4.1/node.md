# N254: 价格红利项 (P_paid_old - P_paid_new) 的量化：在强制价格上限干预 (N18-A) 下，P_paid_new 被截断于 P_median

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

价格红利项 (P_paid_old - P_paid_new) 的量化：在强制价格上限干预 (N18-A) 下，P_paid_new 被截断于 P_median * (1-k)，因此价格红利项下界为 P_median * k，具体数值取决于 k 值（如 k=0.1 时红利为 0.1 * P_median）。

## Corrected Claim

价格红利项 (P_paid_old - P_paid_new) 的量化：在强制价格上限干预 (N18-A) 下，P_paid_new 被截断于 P_median * (1-k)，因此价格红利项下界为 P_median * k，具体数值取决于 k 值（如 k=0.1 时红利为 0.1 * P_median）。

## Evidence

先验知识/题面给定，逻辑校验通过：若 P_paid_new 被截断于 P_median * (1-k)，则 P_paid_old - P_paid_new 的下界确实为 P_median - P_median * (1-k) = P_median * k，数学推导自洽。
