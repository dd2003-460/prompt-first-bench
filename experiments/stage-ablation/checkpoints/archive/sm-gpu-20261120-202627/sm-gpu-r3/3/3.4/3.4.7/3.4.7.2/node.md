# N310: A100 80GB 在持续 LLM 推理负载下的实际平均功耗 P_avg 修正系数：若使用 PCIe 版本，P_avg ≈ 300-350W（低于 SXM 的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

A100 80GB 在持续 LLM 推理负载下的实际平均功耗 P_avg 修正系数：若使用 PCIe 版本，P_avg ≈ 300-350W（低于 SXM 的 400W TDP），需根据具体功耗实测数据修正 OpEx_energy 计算，公式 OpEx_energy = P_avg * 24 * 365 * 3 * E_price。

## Corrected Claim

A100 80GB 在持续 LLM 推理负载下的实际平均功耗 P_avg 修正系数：若使用 PCIe 版本，P_avg ≈ 300-350W（低于 SXM 的 400W TDP），需根据具体功耗实测数据修正 OpEx_energy 计算，公式 OpEx_energy = P_avg * 24 * 365 * 3 * E_price。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 PCIe版TDP通常为300W，SXM版为400W，持续LLM推理负载下平均功耗低于TDP且符合物理直觉，公式量纲正确。
