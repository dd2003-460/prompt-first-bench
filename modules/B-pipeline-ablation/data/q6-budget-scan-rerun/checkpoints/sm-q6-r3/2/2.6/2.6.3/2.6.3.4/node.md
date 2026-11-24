# N230: 年隐性带宽成本差异 Cost_Diff_Annual 计算：Cost_Diff_Annual = ΔF_annual * (Unit_Price_Source_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

年隐性带宽成本差异 Cost_Diff_Annual 计算：Cost_Diff_Annual = ΔF_annual * (Unit_Price_Source_Pub - Unit_Price_Source_Self)，若 ΔF=36.5TB, 价差 ¥0.14/GB，则 Cost_Diff ≈ ¥5,110/年，量化存储投入不足导致的额外支出

## Corrected Claim

年隐性带宽成本差异 Cost_Diff_Annual 计算：Cost_Diff_Annual = ΔF_annual * (Unit_Price_Source_Pub - Unit_Price_Source_Self)，若 ΔF=36.5TB, 价差 ¥0.14/GB，则 Cost_Diff ≈ ¥5,110/年，量化存储投入不足导致的额外支出

## Evidence

先验知识/题面给定，逻辑校验通过：36.5TB = 36500GB，36500 * 0.14 = 5110，计算准确且量纲一致。
