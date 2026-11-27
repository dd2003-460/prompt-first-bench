# N205: 手动降价 N_manual_price_cut 的操作日志定义：指卖家通过前端界面手动修改 P_ask 字段，且修改幅度 ΔP/P_old > 1% 的操作，需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

手动降价 N_manual_price_cut 的操作日志定义：指卖家通过前端界面手动修改 P_ask 字段，且修改幅度 ΔP/P_old > 1% 的操作，需排除系统自动触发的价格同步或库存更新导致的被动价格变动。

## Corrected Claim

手动降价 N_manual_price_cut 的操作日志定义：指卖家通过前端界面手动修改 P_ask 字段，且修改幅度 ΔP/P_old > 1% 的操作，需排除系统自动触发的价格同步或库存更新导致的被动价格变动。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

manual price change definition in e-commerce backend logs
