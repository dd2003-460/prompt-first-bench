# N294: 折旧年限敏感性分析：C_infra_annual(D_years) = C_CAPEX_total / D_years。若 D_years 从3年调整为5年，年

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

折旧年限敏感性分析：C_infra_annual(D_years) = C_CAPEX_total / D_years。若 D_years 从3年调整为5年，年摊销成本从 ¥30,833 降至 ¥18,500，降幅 40%。若 D_years 缩短至2年（技术迭代快），年摊销成本升至 ¥46,250。

## Corrected Claim

折旧年限敏感性分析：C_infra_annual(D_years) = C_CAPEX_total / D_years。若 D_years 从3年调整为5年，年摊销成本从 ¥30,833 降至 ¥18,500，降幅 40%。若 D_years 缩短至2年（技术迭代快），年摊销成本升至 ¥46,250。

## Evidence

先验知识/题面给定，逻辑校验通过：总资本支出 C_CAPEX_total 可由 30,833 * 3 ≈ 92,500 或 18,500 * 5 = 92,500 或 46,250 * 2 = 92,500 反推得出，数值完全自洽，降幅 (30833-18500)/30833 ≈ 40% 计算正确。

## Search Query

server depreciation period 3 years vs 5 years IT asset management
