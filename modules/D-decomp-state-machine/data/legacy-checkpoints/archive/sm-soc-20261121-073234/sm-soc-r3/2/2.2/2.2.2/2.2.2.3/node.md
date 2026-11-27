# N185: ExpectedDays 的估计需引入流动性折扣因子 λ_liquidity，具体公式为 ExpectedDays = 1/(λ_base * λ_liquid

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

ExpectedDays 的估计需引入流动性折扣因子 λ_liquidity，具体公式为 ExpectedDays = 1/(λ_base * λ_liquidity * p_deal)，其中 λ_base 为市场基础成交率，λ_liquidity 反映商品稀缺性（高溢价商品通常 λ_liquidity < 1），当 ExpectedDays 超过 30 天时，c 值将超过卖家心理阈值，触发主动降价行为，这与题面中 60% 卖家降价后无咨询的现象形成因果闭环。

## Corrected Claim

ExpectedDays 的估计需引入流动性折扣因子 λ_liquidity，具体公式为 ExpectedDays = 1/(λ_base * λ_liquidity * p_deal)，其中 λ_base 为市场基础成交率，λ_liquidity 反映商品稀缺性（高溢价商品通常 λ_liquidity < 1）。当 ExpectedDays 超过特定阈值时，c 值将超过卖家心理阈值，触发主动降价行为，这与题面中 60% 卖家降价后无咨询的现象形成因果闭环。

## Evidence

[质询]该陈述包含具体的经验性阈值（30天）和特定的因果机制（60%卖家无咨询），属于经验事实而非第一性原理可推导内容，且参考来源完全不相关，缺乏外部证据支持。 | 参考来源[1]讨论的是基金业协会限售股估值，与本题涉及的二手商品交易流动性折扣及卖家行为模型主题无关，无可用外部证据；但公式逻辑自洽，故降级为定性表述。

## Search Query

second hand market liquidity discount factor expected days to sell high premium items

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/193630728_656666&rut=57d930fdf2345f4361d268304e74c1edc591cf61401aa6d1ecbbb98f606d702f', 'type': 'ddg', 'title': '基金业协会限售股估值excel实现方法 - 搜狐'}
