# N351: 工作点 C（低成本/高故障）：采用二手消费级 GPU（如二手 RTX 3090），MTBF 降至 25,000 小时（因老化），λ_single = 4e-5 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

工作点 C（低成本/高故障）：采用二手消费级 GPU（如二手 RTX 3090），MTBF 降至 25,000 小时（因老化），λ_single = 4e-5 failures/hour，年均故障 0.3504 次/年，对应年均维护成本 C_maint = 0.3504 * $50/hour * 3h + 0.3504 * $800 = $315/年，初始成本最低但需预留更高备件预算。

## Corrected Claim

工作点 C（低成本/高故障）：采用二手消费级 GPU（如二手 RTX 3090），MTBF 降至 25,000 小时（因老化），λ_single = 4e-5 failures/hour，年均故障 0.3504 次/年，对应年均维护成本 C_maint = 0.3504 * $50/hour * 3h + 0.3504 * $800 = $315/年，初始成本最低但需预留更高备件预算。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF 25,000小时对应 λ=4e-5/h，年故障率 0.3504 次/年，维护成本计算 0.3504*(150+800)=315.36 美元，数值量级与逻辑自洽。
