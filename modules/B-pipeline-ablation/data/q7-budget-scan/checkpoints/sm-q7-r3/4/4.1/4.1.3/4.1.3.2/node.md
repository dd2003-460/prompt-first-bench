# N291: 业务中断敏感度系数 Sensitivity_Coeff 的确定：基于历史故障期间的营收损失率或专家评估；若过去 1 小时内数据湖不可用导致 2% 的订单流失，则

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

业务中断敏感度系数 Sensitivity_Coeff 的确定：基于历史故障期间的营收损失率或专家评估；若过去 1 小时内数据湖不可用导致 2% 的订单流失，则系数 = 2% / 100% (假设完全中断) = 0.02，但通常取 0.1-0.5 保守估计，需结合业务关键性调整，核心交易系统取 0.3，非核心报表取 0.1。

## Corrected Claim

业务中断敏感度系数 Sensitivity_Coeff 的确定：基于历史故障期间的营收损失率或专家评估；若过去 1 小时内数据湖不可用导致 2% 的订单流失，则系数 = 2% / 100% (假设完全中断) = 0.02，但通常取 0.1-0.5 保守估计，需结合业务关键性调整，核心交易系统取 0.3，非核心报表取 0.1。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

business interruption sensitivity coefficient calculation
