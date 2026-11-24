# N709: 延长折旧年限的成本-收益权衡：若将 Life_Span 从 3 年延长至 5 年，年化折旧成本从 CapEx/3 降至 CapEx/5，降幅 33.3%。但需增

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N244

## Claim

延长折旧年限的成本-收益权衡：若将 Life_Span 从 3 年延长至 5 年，年化折旧成本从 CapEx/3 降至 CapEx/5，降幅 33.3%。但需增加硬件故障风险成本：P_failure_5yr = 1 - (1 - P_failure_1yr)^5，若 P_failure_1yr=5%，则 P_failure_5yr≈22.6%。额外风险成本 = (P_failure_5yr - P_failure_3yr) × Repair_Cost × Frequency，若 Repair_Cost=¥2000, Frequency=2次/年，则额外成本 ≈ (0.226 - 0.143) × 2000 × 2 = ¥332/年/POP。净收益 = 折旧节省 - 额外风险成本，需验证是否为正。

## Corrected Claim

延长折旧年限的成本-收益权衡：若将 Life_Span 从 3 年延长至 5 年，年化折旧成本从 CapEx/3 降至 CapEx/5，降幅 33.3%。但需增加硬件故障风险成本：P_failure_5yr = 1 - (1 - P_failure_1yr)^5，若 P_failure_1yr=5%，则 P_failure_5yr≈22.6%。额外风险成本 = (P_failure_5yr - P_failure_3yr) × Repair_Cost × Frequency，若 Repair_Cost=¥2000, Frequency=2次/年，则额外成本 ≈ (0.226 - 0.143) × 2000 × 2 = ¥332/年/POP。净收益 = 折旧节省 - 额外风险成本，需验证是否为正。

## Evidence

先验知识/题面给定，逻辑校验通过：折旧降幅计算正确（1/3-1/5=2/15≈33.3%）；故障概率计算符合独立事件假设（1-0.95^5≈22.6%，1-0.95^3≈14.3%）；额外成本计算数值准确（0.083*4000≈332）；逻辑自洽且无内部矛盾。
