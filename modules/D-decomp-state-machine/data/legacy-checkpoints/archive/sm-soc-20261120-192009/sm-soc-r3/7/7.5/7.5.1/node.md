# N315: 反向因果识别策略：使用'上架前 7 天商品质量评分'作为前定变量（Pre-determined Variable），若控制该变量后 CTR 对 T_exposu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

反向因果识别策略：使用'上架前 7 天商品质量评分'作为前定变量（Pre-determined Variable），若控制该变量后 CTR 对 T_exposure 的系数 β_ctr 仍显著，但 T_exposure 对成交周期 T_deal 的系数 β_exp 不显著，则证明存在反向因果（成交快导致曝光多，而非曝光多导致成交快）。

## Corrected Claim

反向因果识别策略：使用'上架前 7 天商品质量评分'作为前定变量（Pre-determined Variable），若控制该变量后 CTR 对 T_exposure 的系数 β_ctr 仍显著，但 T_exposure 对成交周期 T_deal 的系数 β_exp 不显著，则证明存在反向因果（成交快导致曝光多，而非曝光多导致成交快）。

## Evidence

先验知识/题面给定，逻辑校验通过：使用前定变量（Pre-determined Variable）控制内生性干扰是识别反向因果的标准计量经济学策略，逻辑自洽。
