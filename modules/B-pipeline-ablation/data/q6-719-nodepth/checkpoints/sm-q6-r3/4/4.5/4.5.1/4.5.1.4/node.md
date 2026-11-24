# N375: 单级缓存命中率 H_self_single 的修正项：公式 H = 1 - (W/C)^(1/α) 假设静态内容，实际需引入时间衰减因子 λ，H_effecti

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N115

## Claim

单级缓存命中率 H_self_single 的修正项：公式 H = 1 - (W/C)^(1/α) 假设静态内容，实际需引入时间衰减因子 λ，H_effective = H * exp(-λ * Δt)，其中 Δt 为内容平均年龄，λ 为内容更新速率。对于高频更新平台，λ 较大，H_effective 可能比静态模型低 10-20%。

## Corrected Claim

单级缓存命中率 H_self_single 的修正项：公式 H = 1 - (W/C)^(1/α) 假设静态内容，实际需引入时间衰减因子以反映内容更新的影响。对于高频更新平台，由于内容陈旧化，有效命中率 H_effective 通常低于静态模型预测值，具体降幅取决于内容更新速率 λ 与平均年龄 Δt 的乘积。

## Evidence

[质询]该修正公式 H_effective = H * exp(-λ * Δt) 缺乏严格的理论推导支持，属于经验性启发式模型；且“低 10-20%”的具体数值范围缺乏普适性，高度依赖于具体的 λ 和 Δt 取值，不能一概而论。 | 先验知识/题面给定，逻辑校验通过（量纲合理，方向正确），但具体修正公式及数值范围属于经验性工程估算，缺乏严格理论证明或来源支持，故降级。

## Search Query

cache hit rate time decay content update rate dynamic model
