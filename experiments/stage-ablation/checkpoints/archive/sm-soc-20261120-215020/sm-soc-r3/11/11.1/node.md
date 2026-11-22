# N238: 假设 H_signal 的独立性前提检验：需验证 D1（挂价高15-25%）与 D2（成交周期缩短20%）在条件 H_signal 下是否统计独立。若存在交互效

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

假设 H_signal 的独立性前提检验：需验证 D1（挂价高15-25%）与 D2（成交周期缩短20%）在条件 H_signal 下是否统计独立。若存在交互效应（如高挂价导致买家更谨慎，反而延长决策时间），则联合概率 P(D1,D2|H) 不能简单相乘。需计算条件相关系数 ρ_cond = Cov(D1,D2|H_signal) / (σ_D1|H * σ_D2|H)。若 |ρ_cond| > 0.2，则需引入修正项 P(D1,D2|H) = P(D1|H) * P(D2|H) * (1 + ρ_cond * Interaction_Term)，其中 Interaction_Term 需通过平台日志数据估算。

## Corrected Claim

假设 H_signal 的独立性前提检验：需验证 D1（挂价高15-25%）与 D2（成交周期缩短20%）在条件 H_signal 下是否统计独立。若存在交互效应（如高挂价导致买家更谨慎，反而延长决策时间），则联合概率 P(D1,D2|H) 不能简单相乘。需计算条件相关系数 ρ_cond = Cov(D1,D2|H_signal) / (σ_D1|H * σ_D2|H)。若 |ρ_cond| > 0.2，则需引入修正项 P(D1,D2|H) = P(D1|H) * P(D2|H) * (1 + ρ_cond * Interaction_Term)，其中 Interaction_Term 需通过平台日志数据估算。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了统计独立性检验的标准流程（计算条件相关系数并设定阈值），公式结构符合多元统计中处理交互效应的基本逻辑，数值阈值（0.2）为经验性设定，无逻辑矛盾。

## Search Query

conditional dependence probability signal mechanism marketplace economics
