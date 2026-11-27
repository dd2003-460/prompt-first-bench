# N518: 双卡方案2x RTX 3090的3年预期维护成本 E[C_maint_double] 的计算公式：E[C_maint_double] = (P_fail_dou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

双卡方案2x RTX 3090的3年预期维护成本 E[C_maint_double] 的计算公式：E[C_maint_double] = (P_fail_double * 3) * C_repair_double + C_downtime_risk + C_cooling_wear，其中P_fail_double需考虑双卡任一故障即系统不可用的串联可靠性模型，C_downtime_risk为停机业务损失

## Corrected Claim

双卡方案2x RTX 3090的3年预期维护成本 E[C_maint_double] 的计算公式：E[C_maint_double] = (P_fail_double * 3) * C_repair_double + C_downtime_risk + C_cooling_wear，其中P_fail_double需考虑双卡任一故障即系统不可用的串联可靠性模型，C_downtime_risk为停机业务损失

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合可靠性工程基本逻辑（串联系统故障概率、维修成本、停机损失、额外冷却磨损），量纲与逻辑自洽。
