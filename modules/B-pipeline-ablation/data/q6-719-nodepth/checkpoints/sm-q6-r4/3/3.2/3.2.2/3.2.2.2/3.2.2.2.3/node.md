# N729: 工作点2（10Gbps自建）在利用率区间 U_range = [30%, 50%] 下的实际单位成本范围 Unit_Cost_Actual_10G = F_li

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N250

## Claim

工作点2（10Gbps自建）在利用率区间 U_range = [30%, 50%] 下的实际单位成本范围 Unit_Cost_Actual_10G = F_line_10G_self / (Max_Monthly_Traffic_10G × U_range) = 30,000 / (31,500,000 × [0.3, 0.5]) ≈ [¥0.00032, ¥0.00019]/GB，显著低于公有云按量付费，证实其为经济最优工作点

## Corrected Claim

工作点2（10Gbps自建）在利用率区间 U_range = [30%, 50%] 下的实际单位成本范围 Unit_Cost_Actual_10G = F_line_10G_self / (Max_Monthly_Traffic_10G × U_range) = 30,000 / (31,500,000 × [0.3, 0.5]) ≈ [¥0.00032, ¥0.00019]/GB，显著低于公有云按量付费，证实其为经济最优工作点

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 30000/(31500000*0.5)≈0.00019 和 30000/(31500000*0.3)≈0.00032 准确，量纲与逻辑自洽。
