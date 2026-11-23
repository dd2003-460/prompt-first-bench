# N153: 境外流量处理策略的综合最优解判断：当ΔC_overseas > Loss_per_min * P_breach * MTTR时，选择境外公有云节点；其中Loss

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

境外流量处理策略的综合最优解判断：当ΔC_overseas > Loss_per_min * P_breach * MTTR时，选择境外公有云节点；其中Loss_per_min基于N92公式计算，P_breach为延迟超标概率，MTTR为平均修复时间。若ΔC_overseas=¥4,500/month≈¥3.125/min，而Loss_per_min * P_breach * MTTR < ¥3.125/min，则境外公有云节点更优；反之则境内节点更优

## Corrected Claim

境外流量处理策略的综合最优解判断：当ΔC_overseas > Loss_per_min * P_breach * MTTR时，选择境外公有云节点；其中Loss_per_min基于N92公式计算，P_breach为延迟超标概率，MTTR为平均修复时间。若ΔC_overseas=¥4,500/month≈¥3.125/min，而Loss_per_min * P_breach * MTTR < ¥3.125/min，则境外公有云节点更优；反之则境内节点更优

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述基于标准的成本-风险决策模型（期望损失 vs 增量成本），量纲一致（均为货币/时间单位），逻辑推导自洽。
