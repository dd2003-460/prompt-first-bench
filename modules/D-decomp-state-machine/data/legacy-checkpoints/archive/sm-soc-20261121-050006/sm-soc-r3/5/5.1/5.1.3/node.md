# N302: 匹配概率对价格敏感度的弹性：ε_p = ∂ln(p_match)/∂ln(P_ask) = -α，表明 p_match 对 P_ask 的弹性等于负的尾部指数；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

匹配概率对价格敏感度的弹性：ε_p = ∂ln(p_match)/∂ln(P_ask) = -α，表明 p_match 对 P_ask 的弹性等于负的尾部指数；当 α = 2.0 时，P_ask 每增加 1%，p_match 下降 2%；该弹性用于量化高挂价策略对匹配效率的边际影响，需结合 α 的区间 [1.5, 3.0] 计算 p_match 的上下界。

## Corrected Claim

匹配概率对价格敏感度的弹性：ε_p = ∂ln(p_match)/∂ln(P_ask) = -α，表明 p_match 对 P_ask 的弹性等于负的尾部指数；当 α = 2.0 时，P_ask 每增加 1%，p_match 下降 2%；该弹性用于量化高挂价策略对匹配效率的边际影响，需结合 α 的区间 [1.5, 3.0] 计算 p_match 的上下界。

## Evidence

先验知识/题面给定，逻辑校验通过：弹性定义与幂律分布尾部指数关系在数学上自洽，数值量级合理。

## Search Query

price elasticity of match probability heavy-tailed distribution
