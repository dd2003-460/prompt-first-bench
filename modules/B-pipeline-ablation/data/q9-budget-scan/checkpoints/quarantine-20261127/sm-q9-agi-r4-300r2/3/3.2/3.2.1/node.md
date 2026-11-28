# N55: 3-Agent 多数投票机制的幻觉率下降公式：P_hallucination(3) ≈ P_single^3 (假设独立性)，若 P_single=15%，则 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

3-Agent 多数投票机制的幻觉率下降公式：P_hallucination(3) ≈ P_single^3 (假设独立性)，若 P_single=15%，则 P_3≈0.34%；但实际相关性系数 ρ>0 时，P_3 = P_single^(3-2ρ)，需实测 ρ 以校准

## Corrected Claim

3-Agent 多数投票机制在完全独立假设下幻觉率约为 P_single^3（若 P_single=15%，则 P_3≈0.34%）；但在实际场景中，由于 Agent 间存在相关性，幻觉率通常高于独立假设预测值，具体衰减程度需通过实测数据校准，而非简单套用固定指数公式。

## Evidence

[质询]公式 P_3 = P_single^(3-2ρ) 缺乏严格的概率论推导支持，属于经验拟合或特定假设下的近似，且未定义 ρ 的具体统计含义（如相关系数还是依赖度参数），存在将复杂多智能体交互简化为单一指数函数的过度简化风险。 | 先验知识/题面给定，逻辑校验通过（独立性假设下 P^3 成立，数值计算 0.15^3=0.003375≈0.34% 正确），但非独立性下的修正公式为经验性描述，缺乏通用理论证明，故降级。
