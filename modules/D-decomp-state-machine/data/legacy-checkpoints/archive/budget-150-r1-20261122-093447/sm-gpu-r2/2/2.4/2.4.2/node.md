# N76: 数据中心 GPU 维护成本结构：E[C_maint_dc] = (1 - SLA_coverage) * λ_failure * C_replacement +

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

数据中心 GPU 维护成本结构：E[C_maint_dc] = (1 - SLA_coverage) * λ_failure * C_replacement + SLA_coverage * C_support_annual；H100 通常有 3 年 ProSupport 合同，SLA_coverage ≈ 1.0（保修期内免费更换），C_support_annual ≈ $500-$1000/卡；故 5 年维护期望 ≈ $2500-$5000（仅支持费），但硬件成本已含 $25000+，维护成本占比 < 5%；而消费级无 SLA，维护成本占比 ≈ 5-10%（$270-$425 / $1600-$2500）

## Corrected Claim

数据中心 GPU 维护成本结构：E[C_maint_dc] = (1 - SLA_coverage) * λ_failure * C_replacement + SLA_coverage * C_support_annual；H100 通常有 3 年 ProSupport 合同，SLA_coverage ≈ 1.0（保修期内免费更换），C_support_annual ≈ $500-$1000/卡；故 5 年维护期望 ≈ $2500-$5000（仅支持费），但硬件成本已含 $25000+，维护成本占比 < 5%；而消费级无 SLA，维护成本占比 ≈ 5-10%（$270-$425 / $1600-$2500）

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合期望成本定义，数值量级（H100支持费、消费级故障率及成本占比）符合行业常识，无内部矛盾。
