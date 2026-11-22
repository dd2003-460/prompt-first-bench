# N250: 选择偏差对零咨询概率的校正：由于降价卖家非随机样本（见 N90），需引入倾向得分匹配后的校正因子 α_selection；若低价值商品降价概率高，其基准咨询量 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

选择偏差对零咨询概率的校正：由于降价卖家非随机样本（见 N90），需引入倾向得分匹配后的校正因子 α_selection；若低价值商品降价概率高，其基准咨询量 Consult_base_low 较低，则校正后 P(ΔConsult=0 | H2, δ, PSM) = 0.6 / α_selection；若 α_selection = 1.2，则校正后概率为 0.5，更接近理论值 0.535。

## Corrected Claim

选择偏差对零咨询概率的校正：由于降价卖家非随机样本（见 N90），需引入倾向得分匹配后的校正因子 α_selection；若低价值商品降价概率高，其基准咨询量 Consult_base_low 较低，则校正后 P(ΔConsult=0 | H2, δ, PSM) = 0.6 / α_selection；若 α_selection = 1.2，则校正后概率为 0.5，更接近理论值 0.535。

## Evidence

先验知识/题面给定，逻辑校验通过：0.6 / 1.2 = 0.5，且 0.5 与 0.535 的接近性符合描述，数学推导自洽。

## Search Query

propensity score matching correction for selection bias
