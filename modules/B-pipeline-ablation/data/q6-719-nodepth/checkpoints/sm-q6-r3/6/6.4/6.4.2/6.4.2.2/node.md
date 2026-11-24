# N343: Safety_Factor 的敏感性分析：当 H_min 从 70% 降至 60% 时，Peak_Backhaul_Traffic 增加 16.7%，若 Saf

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

Safety_Factor 的敏感性分析：当 H_min 从 70% 降至 60% 时，Peak_Backhaul_Traffic 增加 16.7%，若 Safety_Factor 保持 1.5，则预留带宽不足，需提高至 1.75；反之，若 H_min 稳定在 75%，Safety_Factor 可降至 1.25 以节约成本。成本节约额 ΔC_bw = (1.5-1.25) * Peak_Backhaul_Traffic * P_bw_monthly。

## Corrected Claim

Safety_Factor 的敏感性分析：当 H_min 从 70% 降至 60% 时，Peak_Backhaul_Traffic 增加 16.7%，若 Safety_Factor 保持 1.5，则预留带宽不足，需提高至 1.75；反之，若 H_min 稳定在 75%，Safety_Factor 可降至 1.25 以节约成本。成本节约额 ΔC_bw = (1.5-1.25) * Peak_Backhaul_Traffic * P_bw_monthly。

## Evidence

先验知识/题面给定，逻辑校验通过：1/0.6 - 1/0.7 ≈ 16.7% 符合数学推导；Safety Factor 调整逻辑与成本公式在工程上自洽。
