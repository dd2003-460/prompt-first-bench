# N279: A100 80GB 方案的 5 年维护与 SLA 成本：C_maint_a100 = P_fail_a100 * C_rma + C_sla_gap，其中 P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

A100 80GB 方案的 5 年维护与 SLA 成本：C_maint_a100 = P_fail_a100 * C_rma + C_sla_gap，其中 P_fail_a100 为数据中心卡年故障率 (通常 <1%)，C_rma 为 RMA 处理成本，C_sla_gap 为 SLA 响应间隙内的业务损失，需量化以对比消费级卡的维护优势。

## Corrected Claim

A100 80GB 方案的 5 年维护与 SLA 成本：C_maint_a100 = P_fail_a100 * C_rma + C_sla_gap，其中 P_fail_a100 为数据中心卡年故障率 (通常 <1%)，C_rma 为 RMA 处理成本，C_sla_gap 为 SLA 响应间隙内的业务损失，需量化以对比消费级卡的维护优势。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本工程基本逻辑，A100作为数据中心级GPU，其年故障率通常低于1%符合行业常识，各项成本定义清晰且量纲合理。
