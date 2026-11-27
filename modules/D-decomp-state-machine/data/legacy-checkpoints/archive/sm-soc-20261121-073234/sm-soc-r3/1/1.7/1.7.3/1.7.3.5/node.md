# N167: 当挂价高于成交中位数 20% 时，CVR 的相对下降幅度 ΔCVR/CVR_base ≈ 1 - exp(β1 * ln(1.2))，若 β1 = -0.6，则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

当挂价高于成交中位数 20% 时，CVR 的相对下降幅度 ΔCVR/CVR_base ≈ 1 - exp(β1 * ln(1.2))，若 β1 = -0.6，则下降幅度约为 10.5%；若 β1 = -0.8，则下降幅度约为 13.9%，这与题面 15-25% 的下限吻合但需考虑信任项修正。

## Corrected Claim

当挂价高于成交中位数 20% 时，CVR 的相对下降幅度 ΔCVR/CVR_base ≈ 1 - exp(β1 * ln(1.2))，若 β1 = -0.6，则下降幅度约为 10.5%；若 β1 = -0.8，则下降幅度约为 13.9%，这与题面 15-25% 的下限吻合但需考虑信任项修正。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.6 * ln(1.2)) ≈ 10.5% 和 1 - exp(-0.8 * ln(1.2)) ≈ 13.9% 均正确，且结论与题面范围逻辑自洽。

## Search Query

conversion rate drop 20 percent price premium calculation
