# N531: R_low 场景下的日均总下载量约束验证：若 Hit_Rate = 0.99，则 Origin_Traffic = R_total_low × s_avg × 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N178

## Claim

R_low 场景下的日均总下载量约束验证：若 Hit_Rate = 0.99，则 Origin_Traffic = R_total_low × s_avg × (1 - Hit_Rate) = 100,000,000 × 3.6MB × 0.01 = 3.6TB/天，与题面 2TB/天 不符，表明在 R_low=20 假设下，Hit_Rate 必须 ≥ 99.44% 或 s_avg 需修正为 2.0MB 才能满足 2TB 回源量约束。

## Corrected Claim

R_low 场景下的日均总下载量约束验证：若 Hit_Rate = 0.99，则 Origin_Traffic = R_total_low × s_avg × (1 - Hit_Rate) = 100,000,000 × 3.6MB × 0.01 = 3.6TB/天，与题面 2TB/天 不符，表明在 R_low=20 假设下，Hit_Rate 必须 ≥ 99.44% 或 s_avg 需修正为 2.0MB 才能满足 2TB 回源量约束。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 100,000,000 * 3.6MB * 0.01 = 3.6TB 正确；反推 Hit_Rate >= 1 - 2/3.6 ≈ 99.44% 或 s_avg = 2.0MB 的逻辑推导自洽。
