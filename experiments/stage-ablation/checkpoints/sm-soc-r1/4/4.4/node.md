# N22: 干预对卖家的边际伤害量化：高溢价卖家（markup > 20%）的期望收入损失 ΔRev_seller = P_high * (1 - exp(-λ * Δt)

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

干预对卖家的边际伤害量化：高溢价卖家（markup > 20%）的期望收入损失 ΔRev_seller = P_high * (1 - exp(-λ * Δt)) * (1 - ε_price)，其中 λ 为咨询到达率，ε_price 为价格弹性，需估算 ε_price ∈ [0.5, 1.5] [待核验]

## Corrected Claim

高溢价卖家的期望收入损失 ΔRev_seller 应基于价格调整幅度与需求弹性综合估算，建议采用 ΔRev_seller ≈ P_high * Δt * λ * (1 + ε_price) * ΔP/P 形式（需明确 ΔP 方向），或定性描述为“随咨询到达率 λ 和价格弹性 ε_price 增加而增加”，避免使用导致符号错误的 (1-ε_price) 项。

## Evidence

[质询]公式结构缺乏微观基础：(1-ε_price) 项在 ε_price > 1 时会导致收入损失为负（即收入增加），这与“伤害”的定义矛盾；且将价格弹性直接作为收入损失的线性衰减因子缺乏经济学推导支持，通常收入变化需结合需求弹性与价格变动幅度综合计算。 | 先验知识/题面给定，但逻辑校验发现公式在 ε_price > 1 时违背基本经济直觉（损失为负），且缺乏来源支持该特定函数形式。
