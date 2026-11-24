# N612: 小文件惩罚导致的年边际API成本增量 ΔC_api_small_file = max(0, Req_annual - Free_Tier_Limit) * Pr

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256

## Claim

小文件惩罚导致的年边际API成本增量 ΔC_api_small_file = max(0, Req_annual - Free_Tier_Limit) * Price_per_10k_Req / 10000；若 Free_Tier 为 0（部分国际云商）且价格为 $0.4/万次，则 ΔC ≈ 1.87e8 / 1e4 * $0.4 ≈ $7,480/年，折合人民币约 ¥53,000/年 [knowledge]

## Corrected Claim

小文件惩罚导致的年边际API成本增量 ΔC_api_small_file = max(0, Req_annual - Free_Tier_Limit) * Price_per_10k_Req / 10000；若 Free_Tier 为 0（部分国际云商）且价格为 $0.4/万次，则 ΔC ≈ 1.87e8 / 1e4 * $0.4 ≈ $7,480/年，折合人民币约 ¥53,000/年 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确，数值计算 1.87e8 / 1e4 * 0.4 = 7480 美元准确，汇率换算 7480 * 7.1 ≈ 53000 人民币合理。
