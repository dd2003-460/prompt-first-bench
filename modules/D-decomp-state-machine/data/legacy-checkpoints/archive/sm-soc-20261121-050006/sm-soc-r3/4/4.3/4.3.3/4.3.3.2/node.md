# N281: 置信度修正的贝叶斯公式：Conf_final = Conf_prior * (1 - α_phase_uncertainty)，其中 α_phase_uncer

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

置信度修正的贝叶斯公式：Conf_final = Conf_prior * (1 - α_phase_uncertainty)，其中 α_phase_uncertainty = |g_dau - 0.06| / 0.10（0.06 为增长/成熟期的临界点），当 g_dau = 0.12 时，α_phase_uncertainty = 0.6，导致 Conf_final 从 0.8 下调至 0.32，量化了阶段不确定性对归因置信度的影响。

## Corrected Claim

置信度修正的贝叶斯公式：Conf_final = Conf_prior * (1 - α_phase_uncertainty)，其中 α_phase_uncertainty = |g_dau - 0.06| / 0.10（0.06 为增长/成熟期的临界点），当 g_dau = 0.12 时，α_phase_uncertainty = 0.6，导致 Conf_final 从 0.8 下调至 0.32，量化了阶段不确定性对归因置信度的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，代入数值 g_dau=0.12 计算 α=|0.12-0.06|/0.10=0.6，Conf_final=0.8*(1-0.6)=0.32，数学推导自洽且量级合理。
